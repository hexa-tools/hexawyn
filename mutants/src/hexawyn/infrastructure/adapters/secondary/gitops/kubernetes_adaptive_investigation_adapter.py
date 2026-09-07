from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.ports.driven.adaptive_investigation_port import (
    AdaptiveInvestigationPort,
    ResourceInvestigationRawData,
)
from hexawyn.domain.errors import (
    ClusterUnreachableError,
    InsufficientPermissionsError,
    ResourceNotFoundError,
)

if TYPE_CHECKING:
    from kubernetes.client import CoreV1Api

_K8S_FORBIDDEN = 403
_K8S_NOT_FOUND = 404
_MAX_EVENTS_PER_RESOURCE = 5
_MAX_LOG_LINES_PER_RESOURCE = 20


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut: MutantDict = {}  # type: ignore
mutants_xǁKubernetesAdaptiveInvestigationAdapterǁ_investigate_pod__mutmut: MutantDict = {}  # type: ignore
mutants_xǁKubernetesAdaptiveInvestigationAdapterǁ_verify_deployment_exists__mutmut: MutantDict = {}  # type: ignore
mutants_xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_events__mutmut: MutantDict = {}  # type: ignore
mutants_xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_logs__mutmut: MutantDict = {}  # type: ignore


class KubernetesAdaptiveInvestigationAdapter(AdaptiveInvestigationPort):
    """Secondary adapter — drills into a single failing resource: events,
    container logs, and restart/termination info (reads
    `last_state.terminated.reason` for OOMKilled detection, which none of the
    shallower overview/events/logs adapters read)."""

    @_mutmut_mutated(mutants_xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut)
    def investigate_resource(
        self, namespace: str, kind: str, name: str
    ) -> ResourceInvestigationRawData:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()

        if kind == "Pod":
            restart_count, last_termination_reason, logs = self._investigate_pod(
                k8s, core_api, namespace, name
            )
        else:
            self._verify_deployment_exists(k8s, namespace, name)
            restart_count, last_termination_reason, logs = 0, None, []

        events = self._fetch_events(core_api, namespace, name)

        return ResourceInvestigationRawData(
            events=events,
            logs=logs,
            restart_count=restart_count,
            last_termination_reason=last_termination_reason,
        )

    def xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_orig(
        self, namespace: str, kind: str, name: str
    ) -> ResourceInvestigationRawData:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()

        if kind == "Pod":
            restart_count, last_termination_reason, logs = self._investigate_pod(
                k8s, core_api, namespace, name
            )
        else:
            self._verify_deployment_exists(k8s, namespace, name)
            restart_count, last_termination_reason, logs = 0, None, []

        events = self._fetch_events(core_api, namespace, name)

        return ResourceInvestigationRawData(
            events=events,
            logs=logs,
            restart_count=restart_count,
            last_termination_reason=last_termination_reason,
        )

    def xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_1(
        self, namespace: str, kind: str, name: str
    ) -> ResourceInvestigationRawData:
        from kubernetes import client as k8s

        core_api = None

        if kind == "Pod":
            restart_count, last_termination_reason, logs = self._investigate_pod(
                k8s, core_api, namespace, name
            )
        else:
            self._verify_deployment_exists(k8s, namespace, name)
            restart_count, last_termination_reason, logs = 0, None, []

        events = self._fetch_events(core_api, namespace, name)

        return ResourceInvestigationRawData(
            events=events,
            logs=logs,
            restart_count=restart_count,
            last_termination_reason=last_termination_reason,
        )

    def xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_2(
        self, namespace: str, kind: str, name: str
    ) -> ResourceInvestigationRawData:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()

        if kind != "Pod":
            restart_count, last_termination_reason, logs = self._investigate_pod(
                k8s, core_api, namespace, name
            )
        else:
            self._verify_deployment_exists(k8s, namespace, name)
            restart_count, last_termination_reason, logs = 0, None, []

        events = self._fetch_events(core_api, namespace, name)

        return ResourceInvestigationRawData(
            events=events,
            logs=logs,
            restart_count=restart_count,
            last_termination_reason=last_termination_reason,
        )

    def xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_3(
        self, namespace: str, kind: str, name: str
    ) -> ResourceInvestigationRawData:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()

        if kind == "XXPodXX":
            restart_count, last_termination_reason, logs = self._investigate_pod(
                k8s, core_api, namespace, name
            )
        else:
            self._verify_deployment_exists(k8s, namespace, name)
            restart_count, last_termination_reason, logs = 0, None, []

        events = self._fetch_events(core_api, namespace, name)

        return ResourceInvestigationRawData(
            events=events,
            logs=logs,
            restart_count=restart_count,
            last_termination_reason=last_termination_reason,
        )

    def xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_4(
        self, namespace: str, kind: str, name: str
    ) -> ResourceInvestigationRawData:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()

        if kind == "pod":
            restart_count, last_termination_reason, logs = self._investigate_pod(
                k8s, core_api, namespace, name
            )
        else:
            self._verify_deployment_exists(k8s, namespace, name)
            restart_count, last_termination_reason, logs = 0, None, []

        events = self._fetch_events(core_api, namespace, name)

        return ResourceInvestigationRawData(
            events=events,
            logs=logs,
            restart_count=restart_count,
            last_termination_reason=last_termination_reason,
        )

    def xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_5(
        self, namespace: str, kind: str, name: str
    ) -> ResourceInvestigationRawData:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()

        if kind == "POD":
            restart_count, last_termination_reason, logs = self._investigate_pod(
                k8s, core_api, namespace, name
            )
        else:
            self._verify_deployment_exists(k8s, namespace, name)
            restart_count, last_termination_reason, logs = 0, None, []

        events = self._fetch_events(core_api, namespace, name)

        return ResourceInvestigationRawData(
            events=events,
            logs=logs,
            restart_count=restart_count,
            last_termination_reason=last_termination_reason,
        )

    def xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_6(
        self, namespace: str, kind: str, name: str
    ) -> ResourceInvestigationRawData:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()

        if kind == "Pod":
            restart_count, last_termination_reason, logs = None
        else:
            self._verify_deployment_exists(k8s, namespace, name)
            restart_count, last_termination_reason, logs = 0, None, []

        events = self._fetch_events(core_api, namespace, name)

        return ResourceInvestigationRawData(
            events=events,
            logs=logs,
            restart_count=restart_count,
            last_termination_reason=last_termination_reason,
        )

    def xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_7(
        self, namespace: str, kind: str, name: str
    ) -> ResourceInvestigationRawData:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()

        if kind == "Pod":
            restart_count, last_termination_reason, logs = self._investigate_pod(
                None, core_api, namespace, name
            )
        else:
            self._verify_deployment_exists(k8s, namespace, name)
            restart_count, last_termination_reason, logs = 0, None, []

        events = self._fetch_events(core_api, namespace, name)

        return ResourceInvestigationRawData(
            events=events,
            logs=logs,
            restart_count=restart_count,
            last_termination_reason=last_termination_reason,
        )

    def xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_8(
        self, namespace: str, kind: str, name: str
    ) -> ResourceInvestigationRawData:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()

        if kind == "Pod":
            restart_count, last_termination_reason, logs = self._investigate_pod(
                k8s, None, namespace, name
            )
        else:
            self._verify_deployment_exists(k8s, namespace, name)
            restart_count, last_termination_reason, logs = 0, None, []

        events = self._fetch_events(core_api, namespace, name)

        return ResourceInvestigationRawData(
            events=events,
            logs=logs,
            restart_count=restart_count,
            last_termination_reason=last_termination_reason,
        )

    def xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_9(
        self, namespace: str, kind: str, name: str
    ) -> ResourceInvestigationRawData:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()

        if kind == "Pod":
            restart_count, last_termination_reason, logs = self._investigate_pod(
                k8s, core_api, None, name
            )
        else:
            self._verify_deployment_exists(k8s, namespace, name)
            restart_count, last_termination_reason, logs = 0, None, []

        events = self._fetch_events(core_api, namespace, name)

        return ResourceInvestigationRawData(
            events=events,
            logs=logs,
            restart_count=restart_count,
            last_termination_reason=last_termination_reason,
        )

    def xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_10(
        self, namespace: str, kind: str, name: str
    ) -> ResourceInvestigationRawData:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()

        if kind == "Pod":
            restart_count, last_termination_reason, logs = self._investigate_pod(
                k8s, core_api, namespace, None
            )
        else:
            self._verify_deployment_exists(k8s, namespace, name)
            restart_count, last_termination_reason, logs = 0, None, []

        events = self._fetch_events(core_api, namespace, name)

        return ResourceInvestigationRawData(
            events=events,
            logs=logs,
            restart_count=restart_count,
            last_termination_reason=last_termination_reason,
        )

    def xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_11(
        self, namespace: str, kind: str, name: str
    ) -> ResourceInvestigationRawData:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()

        if kind == "Pod":
            restart_count, last_termination_reason, logs = self._investigate_pod(
                core_api, namespace, name
            )
        else:
            self._verify_deployment_exists(k8s, namespace, name)
            restart_count, last_termination_reason, logs = 0, None, []

        events = self._fetch_events(core_api, namespace, name)

        return ResourceInvestigationRawData(
            events=events,
            logs=logs,
            restart_count=restart_count,
            last_termination_reason=last_termination_reason,
        )

    def xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_12(
        self, namespace: str, kind: str, name: str
    ) -> ResourceInvestigationRawData:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()

        if kind == "Pod":
            restart_count, last_termination_reason, logs = self._investigate_pod(
                k8s, namespace, name
            )
        else:
            self._verify_deployment_exists(k8s, namespace, name)
            restart_count, last_termination_reason, logs = 0, None, []

        events = self._fetch_events(core_api, namespace, name)

        return ResourceInvestigationRawData(
            events=events,
            logs=logs,
            restart_count=restart_count,
            last_termination_reason=last_termination_reason,
        )

    def xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_13(
        self, namespace: str, kind: str, name: str
    ) -> ResourceInvestigationRawData:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()

        if kind == "Pod":
            restart_count, last_termination_reason, logs = self._investigate_pod(
                k8s, core_api, name
            )
        else:
            self._verify_deployment_exists(k8s, namespace, name)
            restart_count, last_termination_reason, logs = 0, None, []

        events = self._fetch_events(core_api, namespace, name)

        return ResourceInvestigationRawData(
            events=events,
            logs=logs,
            restart_count=restart_count,
            last_termination_reason=last_termination_reason,
        )

    def xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_14(
        self, namespace: str, kind: str, name: str
    ) -> ResourceInvestigationRawData:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()

        if kind == "Pod":
            restart_count, last_termination_reason, logs = self._investigate_pod(
                k8s, core_api, namespace, )
        else:
            self._verify_deployment_exists(k8s, namespace, name)
            restart_count, last_termination_reason, logs = 0, None, []

        events = self._fetch_events(core_api, namespace, name)

        return ResourceInvestigationRawData(
            events=events,
            logs=logs,
            restart_count=restart_count,
            last_termination_reason=last_termination_reason,
        )

    def xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_15(
        self, namespace: str, kind: str, name: str
    ) -> ResourceInvestigationRawData:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()

        if kind == "Pod":
            restart_count, last_termination_reason, logs = self._investigate_pod(
                k8s, core_api, namespace, name
            )
        else:
            self._verify_deployment_exists(None, namespace, name)
            restart_count, last_termination_reason, logs = 0, None, []

        events = self._fetch_events(core_api, namespace, name)

        return ResourceInvestigationRawData(
            events=events,
            logs=logs,
            restart_count=restart_count,
            last_termination_reason=last_termination_reason,
        )

    def xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_16(
        self, namespace: str, kind: str, name: str
    ) -> ResourceInvestigationRawData:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()

        if kind == "Pod":
            restart_count, last_termination_reason, logs = self._investigate_pod(
                k8s, core_api, namespace, name
            )
        else:
            self._verify_deployment_exists(k8s, None, name)
            restart_count, last_termination_reason, logs = 0, None, []

        events = self._fetch_events(core_api, namespace, name)

        return ResourceInvestigationRawData(
            events=events,
            logs=logs,
            restart_count=restart_count,
            last_termination_reason=last_termination_reason,
        )

    def xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_17(
        self, namespace: str, kind: str, name: str
    ) -> ResourceInvestigationRawData:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()

        if kind == "Pod":
            restart_count, last_termination_reason, logs = self._investigate_pod(
                k8s, core_api, namespace, name
            )
        else:
            self._verify_deployment_exists(k8s, namespace, None)
            restart_count, last_termination_reason, logs = 0, None, []

        events = self._fetch_events(core_api, namespace, name)

        return ResourceInvestigationRawData(
            events=events,
            logs=logs,
            restart_count=restart_count,
            last_termination_reason=last_termination_reason,
        )

    def xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_18(
        self, namespace: str, kind: str, name: str
    ) -> ResourceInvestigationRawData:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()

        if kind == "Pod":
            restart_count, last_termination_reason, logs = self._investigate_pod(
                k8s, core_api, namespace, name
            )
        else:
            self._verify_deployment_exists(namespace, name)
            restart_count, last_termination_reason, logs = 0, None, []

        events = self._fetch_events(core_api, namespace, name)

        return ResourceInvestigationRawData(
            events=events,
            logs=logs,
            restart_count=restart_count,
            last_termination_reason=last_termination_reason,
        )

    def xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_19(
        self, namespace: str, kind: str, name: str
    ) -> ResourceInvestigationRawData:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()

        if kind == "Pod":
            restart_count, last_termination_reason, logs = self._investigate_pod(
                k8s, core_api, namespace, name
            )
        else:
            self._verify_deployment_exists(k8s, name)
            restart_count, last_termination_reason, logs = 0, None, []

        events = self._fetch_events(core_api, namespace, name)

        return ResourceInvestigationRawData(
            events=events,
            logs=logs,
            restart_count=restart_count,
            last_termination_reason=last_termination_reason,
        )

    def xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_20(
        self, namespace: str, kind: str, name: str
    ) -> ResourceInvestigationRawData:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()

        if kind == "Pod":
            restart_count, last_termination_reason, logs = self._investigate_pod(
                k8s, core_api, namespace, name
            )
        else:
            self._verify_deployment_exists(k8s, namespace, )
            restart_count, last_termination_reason, logs = 0, None, []

        events = self._fetch_events(core_api, namespace, name)

        return ResourceInvestigationRawData(
            events=events,
            logs=logs,
            restart_count=restart_count,
            last_termination_reason=last_termination_reason,
        )

    def xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_21(
        self, namespace: str, kind: str, name: str
    ) -> ResourceInvestigationRawData:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()

        if kind == "Pod":
            restart_count, last_termination_reason, logs = self._investigate_pod(
                k8s, core_api, namespace, name
            )
        else:
            self._verify_deployment_exists(k8s, namespace, name)
            restart_count, last_termination_reason, logs = None

        events = self._fetch_events(core_api, namespace, name)

        return ResourceInvestigationRawData(
            events=events,
            logs=logs,
            restart_count=restart_count,
            last_termination_reason=last_termination_reason,
        )

    def xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_22(
        self, namespace: str, kind: str, name: str
    ) -> ResourceInvestigationRawData:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()

        if kind == "Pod":
            restart_count, last_termination_reason, logs = self._investigate_pod(
                k8s, core_api, namespace, name
            )
        else:
            self._verify_deployment_exists(k8s, namespace, name)
            restart_count, last_termination_reason, logs = 1, None, []

        events = self._fetch_events(core_api, namespace, name)

        return ResourceInvestigationRawData(
            events=events,
            logs=logs,
            restart_count=restart_count,
            last_termination_reason=last_termination_reason,
        )

    def xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_23(
        self, namespace: str, kind: str, name: str
    ) -> ResourceInvestigationRawData:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()

        if kind == "Pod":
            restart_count, last_termination_reason, logs = self._investigate_pod(
                k8s, core_api, namespace, name
            )
        else:
            self._verify_deployment_exists(k8s, namespace, name)
            restart_count, last_termination_reason, logs = 0, None, []

        events = None

        return ResourceInvestigationRawData(
            events=events,
            logs=logs,
            restart_count=restart_count,
            last_termination_reason=last_termination_reason,
        )

    def xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_24(
        self, namespace: str, kind: str, name: str
    ) -> ResourceInvestigationRawData:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()

        if kind == "Pod":
            restart_count, last_termination_reason, logs = self._investigate_pod(
                k8s, core_api, namespace, name
            )
        else:
            self._verify_deployment_exists(k8s, namespace, name)
            restart_count, last_termination_reason, logs = 0, None, []

        events = self._fetch_events(None, namespace, name)

        return ResourceInvestigationRawData(
            events=events,
            logs=logs,
            restart_count=restart_count,
            last_termination_reason=last_termination_reason,
        )

    def xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_25(
        self, namespace: str, kind: str, name: str
    ) -> ResourceInvestigationRawData:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()

        if kind == "Pod":
            restart_count, last_termination_reason, logs = self._investigate_pod(
                k8s, core_api, namespace, name
            )
        else:
            self._verify_deployment_exists(k8s, namespace, name)
            restart_count, last_termination_reason, logs = 0, None, []

        events = self._fetch_events(core_api, None, name)

        return ResourceInvestigationRawData(
            events=events,
            logs=logs,
            restart_count=restart_count,
            last_termination_reason=last_termination_reason,
        )

    def xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_26(
        self, namespace: str, kind: str, name: str
    ) -> ResourceInvestigationRawData:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()

        if kind == "Pod":
            restart_count, last_termination_reason, logs = self._investigate_pod(
                k8s, core_api, namespace, name
            )
        else:
            self._verify_deployment_exists(k8s, namespace, name)
            restart_count, last_termination_reason, logs = 0, None, []

        events = self._fetch_events(core_api, namespace, None)

        return ResourceInvestigationRawData(
            events=events,
            logs=logs,
            restart_count=restart_count,
            last_termination_reason=last_termination_reason,
        )

    def xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_27(
        self, namespace: str, kind: str, name: str
    ) -> ResourceInvestigationRawData:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()

        if kind == "Pod":
            restart_count, last_termination_reason, logs = self._investigate_pod(
                k8s, core_api, namespace, name
            )
        else:
            self._verify_deployment_exists(k8s, namespace, name)
            restart_count, last_termination_reason, logs = 0, None, []

        events = self._fetch_events(namespace, name)

        return ResourceInvestigationRawData(
            events=events,
            logs=logs,
            restart_count=restart_count,
            last_termination_reason=last_termination_reason,
        )

    def xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_28(
        self, namespace: str, kind: str, name: str
    ) -> ResourceInvestigationRawData:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()

        if kind == "Pod":
            restart_count, last_termination_reason, logs = self._investigate_pod(
                k8s, core_api, namespace, name
            )
        else:
            self._verify_deployment_exists(k8s, namespace, name)
            restart_count, last_termination_reason, logs = 0, None, []

        events = self._fetch_events(core_api, name)

        return ResourceInvestigationRawData(
            events=events,
            logs=logs,
            restart_count=restart_count,
            last_termination_reason=last_termination_reason,
        )

    def xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_29(
        self, namespace: str, kind: str, name: str
    ) -> ResourceInvestigationRawData:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()

        if kind == "Pod":
            restart_count, last_termination_reason, logs = self._investigate_pod(
                k8s, core_api, namespace, name
            )
        else:
            self._verify_deployment_exists(k8s, namespace, name)
            restart_count, last_termination_reason, logs = 0, None, []

        events = self._fetch_events(core_api, namespace, )

        return ResourceInvestigationRawData(
            events=events,
            logs=logs,
            restart_count=restart_count,
            last_termination_reason=last_termination_reason,
        )

    def xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_30(
        self, namespace: str, kind: str, name: str
    ) -> ResourceInvestigationRawData:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()

        if kind == "Pod":
            restart_count, last_termination_reason, logs = self._investigate_pod(
                k8s, core_api, namespace, name
            )
        else:
            self._verify_deployment_exists(k8s, namespace, name)
            restart_count, last_termination_reason, logs = 0, None, []

        events = self._fetch_events(core_api, namespace, name)

        return ResourceInvestigationRawData(
            events=None,
            logs=logs,
            restart_count=restart_count,
            last_termination_reason=last_termination_reason,
        )

    def xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_31(
        self, namespace: str, kind: str, name: str
    ) -> ResourceInvestigationRawData:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()

        if kind == "Pod":
            restart_count, last_termination_reason, logs = self._investigate_pod(
                k8s, core_api, namespace, name
            )
        else:
            self._verify_deployment_exists(k8s, namespace, name)
            restart_count, last_termination_reason, logs = 0, None, []

        events = self._fetch_events(core_api, namespace, name)

        return ResourceInvestigationRawData(
            events=events,
            logs=None,
            restart_count=restart_count,
            last_termination_reason=last_termination_reason,
        )

    def xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_32(
        self, namespace: str, kind: str, name: str
    ) -> ResourceInvestigationRawData:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()

        if kind == "Pod":
            restart_count, last_termination_reason, logs = self._investigate_pod(
                k8s, core_api, namespace, name
            )
        else:
            self._verify_deployment_exists(k8s, namespace, name)
            restart_count, last_termination_reason, logs = 0, None, []

        events = self._fetch_events(core_api, namespace, name)

        return ResourceInvestigationRawData(
            events=events,
            logs=logs,
            restart_count=None,
            last_termination_reason=last_termination_reason,
        )

    def xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_33(
        self, namespace: str, kind: str, name: str
    ) -> ResourceInvestigationRawData:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()

        if kind == "Pod":
            restart_count, last_termination_reason, logs = self._investigate_pod(
                k8s, core_api, namespace, name
            )
        else:
            self._verify_deployment_exists(k8s, namespace, name)
            restart_count, last_termination_reason, logs = 0, None, []

        events = self._fetch_events(core_api, namespace, name)

        return ResourceInvestigationRawData(
            events=events,
            logs=logs,
            restart_count=restart_count,
            last_termination_reason=None,
        )

    def xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_34(
        self, namespace: str, kind: str, name: str
    ) -> ResourceInvestigationRawData:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()

        if kind == "Pod":
            restart_count, last_termination_reason, logs = self._investigate_pod(
                k8s, core_api, namespace, name
            )
        else:
            self._verify_deployment_exists(k8s, namespace, name)
            restart_count, last_termination_reason, logs = 0, None, []

        events = self._fetch_events(core_api, namespace, name)

        return ResourceInvestigationRawData(
            logs=logs,
            restart_count=restart_count,
            last_termination_reason=last_termination_reason,
        )

    def xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_35(
        self, namespace: str, kind: str, name: str
    ) -> ResourceInvestigationRawData:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()

        if kind == "Pod":
            restart_count, last_termination_reason, logs = self._investigate_pod(
                k8s, core_api, namespace, name
            )
        else:
            self._verify_deployment_exists(k8s, namespace, name)
            restart_count, last_termination_reason, logs = 0, None, []

        events = self._fetch_events(core_api, namespace, name)

        return ResourceInvestigationRawData(
            events=events,
            restart_count=restart_count,
            last_termination_reason=last_termination_reason,
        )

    def xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_36(
        self, namespace: str, kind: str, name: str
    ) -> ResourceInvestigationRawData:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()

        if kind == "Pod":
            restart_count, last_termination_reason, logs = self._investigate_pod(
                k8s, core_api, namespace, name
            )
        else:
            self._verify_deployment_exists(k8s, namespace, name)
            restart_count, last_termination_reason, logs = 0, None, []

        events = self._fetch_events(core_api, namespace, name)

        return ResourceInvestigationRawData(
            events=events,
            logs=logs,
            last_termination_reason=last_termination_reason,
        )

    def xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_37(
        self, namespace: str, kind: str, name: str
    ) -> ResourceInvestigationRawData:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()

        if kind == "Pod":
            restart_count, last_termination_reason, logs = self._investigate_pod(
                k8s, core_api, namespace, name
            )
        else:
            self._verify_deployment_exists(k8s, namespace, name)
            restart_count, last_termination_reason, logs = 0, None, []

        events = self._fetch_events(core_api, namespace, name)

        return ResourceInvestigationRawData(
            events=events,
            logs=logs,
            restart_count=restart_count,
            )

    @_mutmut_mutated(mutants_xǁKubernetesAdaptiveInvestigationAdapterǁ_investigate_pod__mutmut)
    def _investigate_pod(
        self, k8s: object, core_api: CoreV1Api, namespace: str, name: str
    ) -> tuple[int, str | None, list[str]]:
        try:
            pod = core_api.read_namespaced_pod(name=name, namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc, namespace, name) from exc

        restart_count, last_termination_reason = _extract_container_status(pod)
        logs = self._fetch_logs(core_api, namespace, name)
        return restart_count, last_termination_reason, logs

    def xǁKubernetesAdaptiveInvestigationAdapterǁ_investigate_pod__mutmut_orig(
        self, k8s: object, core_api: CoreV1Api, namespace: str, name: str
    ) -> tuple[int, str | None, list[str]]:
        try:
            pod = core_api.read_namespaced_pod(name=name, namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc, namespace, name) from exc

        restart_count, last_termination_reason = _extract_container_status(pod)
        logs = self._fetch_logs(core_api, namespace, name)
        return restart_count, last_termination_reason, logs

    def xǁKubernetesAdaptiveInvestigationAdapterǁ_investigate_pod__mutmut_1(
        self, k8s: object, core_api: CoreV1Api, namespace: str, name: str
    ) -> tuple[int, str | None, list[str]]:
        try:
            pod = None
        except Exception as exc:
            raise _translate_error(exc, namespace, name) from exc

        restart_count, last_termination_reason = _extract_container_status(pod)
        logs = self._fetch_logs(core_api, namespace, name)
        return restart_count, last_termination_reason, logs

    def xǁKubernetesAdaptiveInvestigationAdapterǁ_investigate_pod__mutmut_2(
        self, k8s: object, core_api: CoreV1Api, namespace: str, name: str
    ) -> tuple[int, str | None, list[str]]:
        try:
            pod = core_api.read_namespaced_pod(name=None, namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc, namespace, name) from exc

        restart_count, last_termination_reason = _extract_container_status(pod)
        logs = self._fetch_logs(core_api, namespace, name)
        return restart_count, last_termination_reason, logs

    def xǁKubernetesAdaptiveInvestigationAdapterǁ_investigate_pod__mutmut_3(
        self, k8s: object, core_api: CoreV1Api, namespace: str, name: str
    ) -> tuple[int, str | None, list[str]]:
        try:
            pod = core_api.read_namespaced_pod(name=name, namespace=None)
        except Exception as exc:
            raise _translate_error(exc, namespace, name) from exc

        restart_count, last_termination_reason = _extract_container_status(pod)
        logs = self._fetch_logs(core_api, namespace, name)
        return restart_count, last_termination_reason, logs

    def xǁKubernetesAdaptiveInvestigationAdapterǁ_investigate_pod__mutmut_4(
        self, k8s: object, core_api: CoreV1Api, namespace: str, name: str
    ) -> tuple[int, str | None, list[str]]:
        try:
            pod = core_api.read_namespaced_pod(namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc, namespace, name) from exc

        restart_count, last_termination_reason = _extract_container_status(pod)
        logs = self._fetch_logs(core_api, namespace, name)
        return restart_count, last_termination_reason, logs

    def xǁKubernetesAdaptiveInvestigationAdapterǁ_investigate_pod__mutmut_5(
        self, k8s: object, core_api: CoreV1Api, namespace: str, name: str
    ) -> tuple[int, str | None, list[str]]:
        try:
            pod = core_api.read_namespaced_pod(name=name, )
        except Exception as exc:
            raise _translate_error(exc, namespace, name) from exc

        restart_count, last_termination_reason = _extract_container_status(pod)
        logs = self._fetch_logs(core_api, namespace, name)
        return restart_count, last_termination_reason, logs

    def xǁKubernetesAdaptiveInvestigationAdapterǁ_investigate_pod__mutmut_6(
        self, k8s: object, core_api: CoreV1Api, namespace: str, name: str
    ) -> tuple[int, str | None, list[str]]:
        try:
            pod = core_api.read_namespaced_pod(name=name, namespace=namespace)
        except Exception as exc:
            raise _translate_error(None, namespace, name) from exc

        restart_count, last_termination_reason = _extract_container_status(pod)
        logs = self._fetch_logs(core_api, namespace, name)
        return restart_count, last_termination_reason, logs

    def xǁKubernetesAdaptiveInvestigationAdapterǁ_investigate_pod__mutmut_7(
        self, k8s: object, core_api: CoreV1Api, namespace: str, name: str
    ) -> tuple[int, str | None, list[str]]:
        try:
            pod = core_api.read_namespaced_pod(name=name, namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc, None, name) from exc

        restart_count, last_termination_reason = _extract_container_status(pod)
        logs = self._fetch_logs(core_api, namespace, name)
        return restart_count, last_termination_reason, logs

    def xǁKubernetesAdaptiveInvestigationAdapterǁ_investigate_pod__mutmut_8(
        self, k8s: object, core_api: CoreV1Api, namespace: str, name: str
    ) -> tuple[int, str | None, list[str]]:
        try:
            pod = core_api.read_namespaced_pod(name=name, namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc, namespace, None) from exc

        restart_count, last_termination_reason = _extract_container_status(pod)
        logs = self._fetch_logs(core_api, namespace, name)
        return restart_count, last_termination_reason, logs

    def xǁKubernetesAdaptiveInvestigationAdapterǁ_investigate_pod__mutmut_9(
        self, k8s: object, core_api: CoreV1Api, namespace: str, name: str
    ) -> tuple[int, str | None, list[str]]:
        try:
            pod = core_api.read_namespaced_pod(name=name, namespace=namespace)
        except Exception as exc:
            raise _translate_error(namespace, name) from exc

        restart_count, last_termination_reason = _extract_container_status(pod)
        logs = self._fetch_logs(core_api, namespace, name)
        return restart_count, last_termination_reason, logs

    def xǁKubernetesAdaptiveInvestigationAdapterǁ_investigate_pod__mutmut_10(
        self, k8s: object, core_api: CoreV1Api, namespace: str, name: str
    ) -> tuple[int, str | None, list[str]]:
        try:
            pod = core_api.read_namespaced_pod(name=name, namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc, name) from exc

        restart_count, last_termination_reason = _extract_container_status(pod)
        logs = self._fetch_logs(core_api, namespace, name)
        return restart_count, last_termination_reason, logs

    def xǁKubernetesAdaptiveInvestigationAdapterǁ_investigate_pod__mutmut_11(
        self, k8s: object, core_api: CoreV1Api, namespace: str, name: str
    ) -> tuple[int, str | None, list[str]]:
        try:
            pod = core_api.read_namespaced_pod(name=name, namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc, namespace, ) from exc

        restart_count, last_termination_reason = _extract_container_status(pod)
        logs = self._fetch_logs(core_api, namespace, name)
        return restart_count, last_termination_reason, logs

    def xǁKubernetesAdaptiveInvestigationAdapterǁ_investigate_pod__mutmut_12(
        self, k8s: object, core_api: CoreV1Api, namespace: str, name: str
    ) -> tuple[int, str | None, list[str]]:
        try:
            pod = core_api.read_namespaced_pod(name=name, namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc, namespace, name) from exc

        restart_count, last_termination_reason = None
        logs = self._fetch_logs(core_api, namespace, name)
        return restart_count, last_termination_reason, logs

    def xǁKubernetesAdaptiveInvestigationAdapterǁ_investigate_pod__mutmut_13(
        self, k8s: object, core_api: CoreV1Api, namespace: str, name: str
    ) -> tuple[int, str | None, list[str]]:
        try:
            pod = core_api.read_namespaced_pod(name=name, namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc, namespace, name) from exc

        restart_count, last_termination_reason = _extract_container_status(None)
        logs = self._fetch_logs(core_api, namespace, name)
        return restart_count, last_termination_reason, logs

    def xǁKubernetesAdaptiveInvestigationAdapterǁ_investigate_pod__mutmut_14(
        self, k8s: object, core_api: CoreV1Api, namespace: str, name: str
    ) -> tuple[int, str | None, list[str]]:
        try:
            pod = core_api.read_namespaced_pod(name=name, namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc, namespace, name) from exc

        restart_count, last_termination_reason = _extract_container_status(pod)
        logs = None
        return restart_count, last_termination_reason, logs

    def xǁKubernetesAdaptiveInvestigationAdapterǁ_investigate_pod__mutmut_15(
        self, k8s: object, core_api: CoreV1Api, namespace: str, name: str
    ) -> tuple[int, str | None, list[str]]:
        try:
            pod = core_api.read_namespaced_pod(name=name, namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc, namespace, name) from exc

        restart_count, last_termination_reason = _extract_container_status(pod)
        logs = self._fetch_logs(None, namespace, name)
        return restart_count, last_termination_reason, logs

    def xǁKubernetesAdaptiveInvestigationAdapterǁ_investigate_pod__mutmut_16(
        self, k8s: object, core_api: CoreV1Api, namespace: str, name: str
    ) -> tuple[int, str | None, list[str]]:
        try:
            pod = core_api.read_namespaced_pod(name=name, namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc, namespace, name) from exc

        restart_count, last_termination_reason = _extract_container_status(pod)
        logs = self._fetch_logs(core_api, None, name)
        return restart_count, last_termination_reason, logs

    def xǁKubernetesAdaptiveInvestigationAdapterǁ_investigate_pod__mutmut_17(
        self, k8s: object, core_api: CoreV1Api, namespace: str, name: str
    ) -> tuple[int, str | None, list[str]]:
        try:
            pod = core_api.read_namespaced_pod(name=name, namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc, namespace, name) from exc

        restart_count, last_termination_reason = _extract_container_status(pod)
        logs = self._fetch_logs(core_api, namespace, None)
        return restart_count, last_termination_reason, logs

    def xǁKubernetesAdaptiveInvestigationAdapterǁ_investigate_pod__mutmut_18(
        self, k8s: object, core_api: CoreV1Api, namespace: str, name: str
    ) -> tuple[int, str | None, list[str]]:
        try:
            pod = core_api.read_namespaced_pod(name=name, namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc, namespace, name) from exc

        restart_count, last_termination_reason = _extract_container_status(pod)
        logs = self._fetch_logs(namespace, name)
        return restart_count, last_termination_reason, logs

    def xǁKubernetesAdaptiveInvestigationAdapterǁ_investigate_pod__mutmut_19(
        self, k8s: object, core_api: CoreV1Api, namespace: str, name: str
    ) -> tuple[int, str | None, list[str]]:
        try:
            pod = core_api.read_namespaced_pod(name=name, namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc, namespace, name) from exc

        restart_count, last_termination_reason = _extract_container_status(pod)
        logs = self._fetch_logs(core_api, name)
        return restart_count, last_termination_reason, logs

    def xǁKubernetesAdaptiveInvestigationAdapterǁ_investigate_pod__mutmut_20(
        self, k8s: object, core_api: CoreV1Api, namespace: str, name: str
    ) -> tuple[int, str | None, list[str]]:
        try:
            pod = core_api.read_namespaced_pod(name=name, namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc, namespace, name) from exc

        restart_count, last_termination_reason = _extract_container_status(pod)
        logs = self._fetch_logs(core_api, namespace, )
        return restart_count, last_termination_reason, logs

    @_mutmut_mutated(mutants_xǁKubernetesAdaptiveInvestigationAdapterǁ_verify_deployment_exists__mutmut)
    def _verify_deployment_exists(self, k8s: object, namespace: str, name: str) -> None:
        apps_api = k8s.AppsV1Api()  # type: ignore[attr-defined]
        try:
            apps_api.read_namespaced_deployment(name=name, namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc, namespace, name) from exc

    def xǁKubernetesAdaptiveInvestigationAdapterǁ_verify_deployment_exists__mutmut_orig(self, k8s: object, namespace: str, name: str) -> None:
        apps_api = k8s.AppsV1Api()  # type: ignore[attr-defined]
        try:
            apps_api.read_namespaced_deployment(name=name, namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc, namespace, name) from exc

    def xǁKubernetesAdaptiveInvestigationAdapterǁ_verify_deployment_exists__mutmut_1(self, k8s: object, namespace: str, name: str) -> None:
        apps_api = None  # type: ignore[attr-defined]
        try:
            apps_api.read_namespaced_deployment(name=name, namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc, namespace, name) from exc

    def xǁKubernetesAdaptiveInvestigationAdapterǁ_verify_deployment_exists__mutmut_2(self, k8s: object, namespace: str, name: str) -> None:
        apps_api = k8s.AppsV1Api()  # type: ignore[attr-defined]
        try:
            apps_api.read_namespaced_deployment(name=None, namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc, namespace, name) from exc

    def xǁKubernetesAdaptiveInvestigationAdapterǁ_verify_deployment_exists__mutmut_3(self, k8s: object, namespace: str, name: str) -> None:
        apps_api = k8s.AppsV1Api()  # type: ignore[attr-defined]
        try:
            apps_api.read_namespaced_deployment(name=name, namespace=None)
        except Exception as exc:
            raise _translate_error(exc, namespace, name) from exc

    def xǁKubernetesAdaptiveInvestigationAdapterǁ_verify_deployment_exists__mutmut_4(self, k8s: object, namespace: str, name: str) -> None:
        apps_api = k8s.AppsV1Api()  # type: ignore[attr-defined]
        try:
            apps_api.read_namespaced_deployment(namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc, namespace, name) from exc

    def xǁKubernetesAdaptiveInvestigationAdapterǁ_verify_deployment_exists__mutmut_5(self, k8s: object, namespace: str, name: str) -> None:
        apps_api = k8s.AppsV1Api()  # type: ignore[attr-defined]
        try:
            apps_api.read_namespaced_deployment(name=name, )
        except Exception as exc:
            raise _translate_error(exc, namespace, name) from exc

    def xǁKubernetesAdaptiveInvestigationAdapterǁ_verify_deployment_exists__mutmut_6(self, k8s: object, namespace: str, name: str) -> None:
        apps_api = k8s.AppsV1Api()  # type: ignore[attr-defined]
        try:
            apps_api.read_namespaced_deployment(name=name, namespace=namespace)
        except Exception as exc:
            raise _translate_error(None, namespace, name) from exc

    def xǁKubernetesAdaptiveInvestigationAdapterǁ_verify_deployment_exists__mutmut_7(self, k8s: object, namespace: str, name: str) -> None:
        apps_api = k8s.AppsV1Api()  # type: ignore[attr-defined]
        try:
            apps_api.read_namespaced_deployment(name=name, namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc, None, name) from exc

    def xǁKubernetesAdaptiveInvestigationAdapterǁ_verify_deployment_exists__mutmut_8(self, k8s: object, namespace: str, name: str) -> None:
        apps_api = k8s.AppsV1Api()  # type: ignore[attr-defined]
        try:
            apps_api.read_namespaced_deployment(name=name, namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc, namespace, None) from exc

    def xǁKubernetesAdaptiveInvestigationAdapterǁ_verify_deployment_exists__mutmut_9(self, k8s: object, namespace: str, name: str) -> None:
        apps_api = k8s.AppsV1Api()  # type: ignore[attr-defined]
        try:
            apps_api.read_namespaced_deployment(name=name, namespace=namespace)
        except Exception as exc:
            raise _translate_error(namespace, name) from exc

    def xǁKubernetesAdaptiveInvestigationAdapterǁ_verify_deployment_exists__mutmut_10(self, k8s: object, namespace: str, name: str) -> None:
        apps_api = k8s.AppsV1Api()  # type: ignore[attr-defined]
        try:
            apps_api.read_namespaced_deployment(name=name, namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc, name) from exc

    def xǁKubernetesAdaptiveInvestigationAdapterǁ_verify_deployment_exists__mutmut_11(self, k8s: object, namespace: str, name: str) -> None:
        apps_api = k8s.AppsV1Api()  # type: ignore[attr-defined]
        try:
            apps_api.read_namespaced_deployment(name=name, namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc, namespace, ) from exc

    @_mutmut_mutated(mutants_xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_events__mutmut)
    def _fetch_events(self, core_api: CoreV1Api, namespace: str, name: str) -> list[str]:
        try:
            event_list = core_api.list_namespaced_event(namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc, namespace, name) from exc

        matching = [item for item in event_list.items if item.involved_object.name == name]
        top = matching[:_MAX_EVENTS_PER_RESOURCE]
        return [f"{item.reason}: {item.message} (x{item.count or 1})" for item in top]

    def xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_events__mutmut_orig(self, core_api: CoreV1Api, namespace: str, name: str) -> list[str]:
        try:
            event_list = core_api.list_namespaced_event(namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc, namespace, name) from exc

        matching = [item for item in event_list.items if item.involved_object.name == name]
        top = matching[:_MAX_EVENTS_PER_RESOURCE]
        return [f"{item.reason}: {item.message} (x{item.count or 1})" for item in top]

    def xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_events__mutmut_1(self, core_api: CoreV1Api, namespace: str, name: str) -> list[str]:
        try:
            event_list = None
        except Exception as exc:
            raise _translate_error(exc, namespace, name) from exc

        matching = [item for item in event_list.items if item.involved_object.name == name]
        top = matching[:_MAX_EVENTS_PER_RESOURCE]
        return [f"{item.reason}: {item.message} (x{item.count or 1})" for item in top]

    def xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_events__mutmut_2(self, core_api: CoreV1Api, namespace: str, name: str) -> list[str]:
        try:
            event_list = core_api.list_namespaced_event(namespace=None)
        except Exception as exc:
            raise _translate_error(exc, namespace, name) from exc

        matching = [item for item in event_list.items if item.involved_object.name == name]
        top = matching[:_MAX_EVENTS_PER_RESOURCE]
        return [f"{item.reason}: {item.message} (x{item.count or 1})" for item in top]

    def xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_events__mutmut_3(self, core_api: CoreV1Api, namespace: str, name: str) -> list[str]:
        try:
            event_list = core_api.list_namespaced_event(namespace=namespace)
        except Exception as exc:
            raise _translate_error(None, namespace, name) from exc

        matching = [item for item in event_list.items if item.involved_object.name == name]
        top = matching[:_MAX_EVENTS_PER_RESOURCE]
        return [f"{item.reason}: {item.message} (x{item.count or 1})" for item in top]

    def xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_events__mutmut_4(self, core_api: CoreV1Api, namespace: str, name: str) -> list[str]:
        try:
            event_list = core_api.list_namespaced_event(namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc, None, name) from exc

        matching = [item for item in event_list.items if item.involved_object.name == name]
        top = matching[:_MAX_EVENTS_PER_RESOURCE]
        return [f"{item.reason}: {item.message} (x{item.count or 1})" for item in top]

    def xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_events__mutmut_5(self, core_api: CoreV1Api, namespace: str, name: str) -> list[str]:
        try:
            event_list = core_api.list_namespaced_event(namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc, namespace, None) from exc

        matching = [item for item in event_list.items if item.involved_object.name == name]
        top = matching[:_MAX_EVENTS_PER_RESOURCE]
        return [f"{item.reason}: {item.message} (x{item.count or 1})" for item in top]

    def xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_events__mutmut_6(self, core_api: CoreV1Api, namespace: str, name: str) -> list[str]:
        try:
            event_list = core_api.list_namespaced_event(namespace=namespace)
        except Exception as exc:
            raise _translate_error(namespace, name) from exc

        matching = [item for item in event_list.items if item.involved_object.name == name]
        top = matching[:_MAX_EVENTS_PER_RESOURCE]
        return [f"{item.reason}: {item.message} (x{item.count or 1})" for item in top]

    def xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_events__mutmut_7(self, core_api: CoreV1Api, namespace: str, name: str) -> list[str]:
        try:
            event_list = core_api.list_namespaced_event(namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc, name) from exc

        matching = [item for item in event_list.items if item.involved_object.name == name]
        top = matching[:_MAX_EVENTS_PER_RESOURCE]
        return [f"{item.reason}: {item.message} (x{item.count or 1})" for item in top]

    def xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_events__mutmut_8(self, core_api: CoreV1Api, namespace: str, name: str) -> list[str]:
        try:
            event_list = core_api.list_namespaced_event(namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc, namespace, ) from exc

        matching = [item for item in event_list.items if item.involved_object.name == name]
        top = matching[:_MAX_EVENTS_PER_RESOURCE]
        return [f"{item.reason}: {item.message} (x{item.count or 1})" for item in top]

    def xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_events__mutmut_9(self, core_api: CoreV1Api, namespace: str, name: str) -> list[str]:
        try:
            event_list = core_api.list_namespaced_event(namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc, namespace, name) from exc

        matching = None
        top = matching[:_MAX_EVENTS_PER_RESOURCE]
        return [f"{item.reason}: {item.message} (x{item.count or 1})" for item in top]

    def xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_events__mutmut_10(self, core_api: CoreV1Api, namespace: str, name: str) -> list[str]:
        try:
            event_list = core_api.list_namespaced_event(namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc, namespace, name) from exc

        matching = [item for item in event_list.items if item.involved_object.name != name]
        top = matching[:_MAX_EVENTS_PER_RESOURCE]
        return [f"{item.reason}: {item.message} (x{item.count or 1})" for item in top]

    def xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_events__mutmut_11(self, core_api: CoreV1Api, namespace: str, name: str) -> list[str]:
        try:
            event_list = core_api.list_namespaced_event(namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc, namespace, name) from exc

        matching = [item for item in event_list.items if item.involved_object.name == name]
        top = None
        return [f"{item.reason}: {item.message} (x{item.count or 1})" for item in top]

    def xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_events__mutmut_12(self, core_api: CoreV1Api, namespace: str, name: str) -> list[str]:
        try:
            event_list = core_api.list_namespaced_event(namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc, namespace, name) from exc

        matching = [item for item in event_list.items if item.involved_object.name == name]
        top = matching[:_MAX_EVENTS_PER_RESOURCE]
        return [f"{item.reason}: {item.message} (x{item.count and 1})" for item in top]

    def xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_events__mutmut_13(self, core_api: CoreV1Api, namespace: str, name: str) -> list[str]:
        try:
            event_list = core_api.list_namespaced_event(namespace=namespace)
        except Exception as exc:
            raise _translate_error(exc, namespace, name) from exc

        matching = [item for item in event_list.items if item.involved_object.name == name]
        top = matching[:_MAX_EVENTS_PER_RESOURCE]
        return [f"{item.reason}: {item.message} (x{item.count or 2})" for item in top]

    @_mutmut_mutated(mutants_xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_logs__mutmut)
    def _fetch_logs(self, core_api: CoreV1Api, namespace: str, name: str) -> list[str]:
        try:
            response = core_api.read_namespaced_pod_log(
                name=name,
                namespace=namespace,
                tail_lines=_MAX_LOG_LINES_PER_RESOURCE,
                _preload_content=False,
            )
        except Exception:
            return []
        raw_bytes: bytes = response.data
        text = raw_bytes.decode("utf-8", errors="replace")
        return [line for line in text.splitlines() if line.strip()]

    def xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_logs__mutmut_orig(self, core_api: CoreV1Api, namespace: str, name: str) -> list[str]:
        try:
            response = core_api.read_namespaced_pod_log(
                name=name,
                namespace=namespace,
                tail_lines=_MAX_LOG_LINES_PER_RESOURCE,
                _preload_content=False,
            )
        except Exception:
            return []
        raw_bytes: bytes = response.data
        text = raw_bytes.decode("utf-8", errors="replace")
        return [line for line in text.splitlines() if line.strip()]

    def xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_logs__mutmut_1(self, core_api: CoreV1Api, namespace: str, name: str) -> list[str]:
        try:
            response = None
        except Exception:
            return []
        raw_bytes: bytes = response.data
        text = raw_bytes.decode("utf-8", errors="replace")
        return [line for line in text.splitlines() if line.strip()]

    def xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_logs__mutmut_2(self, core_api: CoreV1Api, namespace: str, name: str) -> list[str]:
        try:
            response = core_api.read_namespaced_pod_log(
                name=None,
                namespace=namespace,
                tail_lines=_MAX_LOG_LINES_PER_RESOURCE,
                _preload_content=False,
            )
        except Exception:
            return []
        raw_bytes: bytes = response.data
        text = raw_bytes.decode("utf-8", errors="replace")
        return [line for line in text.splitlines() if line.strip()]

    def xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_logs__mutmut_3(self, core_api: CoreV1Api, namespace: str, name: str) -> list[str]:
        try:
            response = core_api.read_namespaced_pod_log(
                name=name,
                namespace=None,
                tail_lines=_MAX_LOG_LINES_PER_RESOURCE,
                _preload_content=False,
            )
        except Exception:
            return []
        raw_bytes: bytes = response.data
        text = raw_bytes.decode("utf-8", errors="replace")
        return [line for line in text.splitlines() if line.strip()]

    def xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_logs__mutmut_4(self, core_api: CoreV1Api, namespace: str, name: str) -> list[str]:
        try:
            response = core_api.read_namespaced_pod_log(
                name=name,
                namespace=namespace,
                tail_lines=None,
                _preload_content=False,
            )
        except Exception:
            return []
        raw_bytes: bytes = response.data
        text = raw_bytes.decode("utf-8", errors="replace")
        return [line for line in text.splitlines() if line.strip()]

    def xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_logs__mutmut_5(self, core_api: CoreV1Api, namespace: str, name: str) -> list[str]:
        try:
            response = core_api.read_namespaced_pod_log(
                name=name,
                namespace=namespace,
                tail_lines=_MAX_LOG_LINES_PER_RESOURCE,
                _preload_content=None,
            )
        except Exception:
            return []
        raw_bytes: bytes = response.data
        text = raw_bytes.decode("utf-8", errors="replace")
        return [line for line in text.splitlines() if line.strip()]

    def xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_logs__mutmut_6(self, core_api: CoreV1Api, namespace: str, name: str) -> list[str]:
        try:
            response = core_api.read_namespaced_pod_log(
                namespace=namespace,
                tail_lines=_MAX_LOG_LINES_PER_RESOURCE,
                _preload_content=False,
            )
        except Exception:
            return []
        raw_bytes: bytes = response.data
        text = raw_bytes.decode("utf-8", errors="replace")
        return [line for line in text.splitlines() if line.strip()]

    def xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_logs__mutmut_7(self, core_api: CoreV1Api, namespace: str, name: str) -> list[str]:
        try:
            response = core_api.read_namespaced_pod_log(
                name=name,
                tail_lines=_MAX_LOG_LINES_PER_RESOURCE,
                _preload_content=False,
            )
        except Exception:
            return []
        raw_bytes: bytes = response.data
        text = raw_bytes.decode("utf-8", errors="replace")
        return [line for line in text.splitlines() if line.strip()]

    def xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_logs__mutmut_8(self, core_api: CoreV1Api, namespace: str, name: str) -> list[str]:
        try:
            response = core_api.read_namespaced_pod_log(
                name=name,
                namespace=namespace,
                _preload_content=False,
            )
        except Exception:
            return []
        raw_bytes: bytes = response.data
        text = raw_bytes.decode("utf-8", errors="replace")
        return [line for line in text.splitlines() if line.strip()]

    def xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_logs__mutmut_9(self, core_api: CoreV1Api, namespace: str, name: str) -> list[str]:
        try:
            response = core_api.read_namespaced_pod_log(
                name=name,
                namespace=namespace,
                tail_lines=_MAX_LOG_LINES_PER_RESOURCE,
                )
        except Exception:
            return []
        raw_bytes: bytes = response.data
        text = raw_bytes.decode("utf-8", errors="replace")
        return [line for line in text.splitlines() if line.strip()]

    def xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_logs__mutmut_10(self, core_api: CoreV1Api, namespace: str, name: str) -> list[str]:
        try:
            response = core_api.read_namespaced_pod_log(
                name=name,
                namespace=namespace,
                tail_lines=_MAX_LOG_LINES_PER_RESOURCE,
                _preload_content=True,
            )
        except Exception:
            return []
        raw_bytes: bytes = response.data
        text = raw_bytes.decode("utf-8", errors="replace")
        return [line for line in text.splitlines() if line.strip()]

    def xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_logs__mutmut_11(self, core_api: CoreV1Api, namespace: str, name: str) -> list[str]:
        try:
            response = core_api.read_namespaced_pod_log(
                name=name,
                namespace=namespace,
                tail_lines=_MAX_LOG_LINES_PER_RESOURCE,
                _preload_content=False,
            )
        except Exception:
            return []
        raw_bytes: bytes = None
        text = raw_bytes.decode("utf-8", errors="replace")
        return [line for line in text.splitlines() if line.strip()]

    def xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_logs__mutmut_12(self, core_api: CoreV1Api, namespace: str, name: str) -> list[str]:
        try:
            response = core_api.read_namespaced_pod_log(
                name=name,
                namespace=namespace,
                tail_lines=_MAX_LOG_LINES_PER_RESOURCE,
                _preload_content=False,
            )
        except Exception:
            return []
        raw_bytes: bytes = response.data
        text = None
        return [line for line in text.splitlines() if line.strip()]

    def xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_logs__mutmut_13(self, core_api: CoreV1Api, namespace: str, name: str) -> list[str]:
        try:
            response = core_api.read_namespaced_pod_log(
                name=name,
                namespace=namespace,
                tail_lines=_MAX_LOG_LINES_PER_RESOURCE,
                _preload_content=False,
            )
        except Exception:
            return []
        raw_bytes: bytes = response.data
        text = raw_bytes.decode(None, errors="replace")
        return [line for line in text.splitlines() if line.strip()]

    def xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_logs__mutmut_14(self, core_api: CoreV1Api, namespace: str, name: str) -> list[str]:
        try:
            response = core_api.read_namespaced_pod_log(
                name=name,
                namespace=namespace,
                tail_lines=_MAX_LOG_LINES_PER_RESOURCE,
                _preload_content=False,
            )
        except Exception:
            return []
        raw_bytes: bytes = response.data
        text = raw_bytes.decode("utf-8", errors=None)
        return [line for line in text.splitlines() if line.strip()]

    def xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_logs__mutmut_15(self, core_api: CoreV1Api, namespace: str, name: str) -> list[str]:
        try:
            response = core_api.read_namespaced_pod_log(
                name=name,
                namespace=namespace,
                tail_lines=_MAX_LOG_LINES_PER_RESOURCE,
                _preload_content=False,
            )
        except Exception:
            return []
        raw_bytes: bytes = response.data
        text = raw_bytes.decode(errors="replace")
        return [line for line in text.splitlines() if line.strip()]

    def xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_logs__mutmut_16(self, core_api: CoreV1Api, namespace: str, name: str) -> list[str]:
        try:
            response = core_api.read_namespaced_pod_log(
                name=name,
                namespace=namespace,
                tail_lines=_MAX_LOG_LINES_PER_RESOURCE,
                _preload_content=False,
            )
        except Exception:
            return []
        raw_bytes: bytes = response.data
        text = raw_bytes.decode("utf-8", )
        return [line for line in text.splitlines() if line.strip()]

    def xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_logs__mutmut_17(self, core_api: CoreV1Api, namespace: str, name: str) -> list[str]:
        try:
            response = core_api.read_namespaced_pod_log(
                name=name,
                namespace=namespace,
                tail_lines=_MAX_LOG_LINES_PER_RESOURCE,
                _preload_content=False,
            )
        except Exception:
            return []
        raw_bytes: bytes = response.data
        text = raw_bytes.decode("XXutf-8XX", errors="replace")
        return [line for line in text.splitlines() if line.strip()]

    def xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_logs__mutmut_18(self, core_api: CoreV1Api, namespace: str, name: str) -> list[str]:
        try:
            response = core_api.read_namespaced_pod_log(
                name=name,
                namespace=namespace,
                tail_lines=_MAX_LOG_LINES_PER_RESOURCE,
                _preload_content=False,
            )
        except Exception:
            return []
        raw_bytes: bytes = response.data
        text = raw_bytes.decode("UTF-8", errors="replace")
        return [line for line in text.splitlines() if line.strip()]

    def xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_logs__mutmut_19(self, core_api: CoreV1Api, namespace: str, name: str) -> list[str]:
        try:
            response = core_api.read_namespaced_pod_log(
                name=name,
                namespace=namespace,
                tail_lines=_MAX_LOG_LINES_PER_RESOURCE,
                _preload_content=False,
            )
        except Exception:
            return []
        raw_bytes: bytes = response.data
        text = raw_bytes.decode("utf-8", errors="XXreplaceXX")
        return [line for line in text.splitlines() if line.strip()]

    def xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_logs__mutmut_20(self, core_api: CoreV1Api, namespace: str, name: str) -> list[str]:
        try:
            response = core_api.read_namespaced_pod_log(
                name=name,
                namespace=namespace,
                tail_lines=_MAX_LOG_LINES_PER_RESOURCE,
                _preload_content=False,
            )
        except Exception:
            return []
        raw_bytes: bytes = response.data
        text = raw_bytes.decode("utf-8", errors="REPLACE")
        return [line for line in text.splitlines() if line.strip()]

mutants_xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut['_mutmut_orig'] = KubernetesAdaptiveInvestigationAdapter.xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_orig # type: ignore # mutmut generated
mutants_xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut['xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_1'] = KubernetesAdaptiveInvestigationAdapter.xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_1 # type: ignore # mutmut generated
mutants_xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut['xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_2'] = KubernetesAdaptiveInvestigationAdapter.xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_2 # type: ignore # mutmut generated
mutants_xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut['xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_3'] = KubernetesAdaptiveInvestigationAdapter.xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_3 # type: ignore # mutmut generated
mutants_xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut['xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_4'] = KubernetesAdaptiveInvestigationAdapter.xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_4 # type: ignore # mutmut generated
mutants_xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut['xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_5'] = KubernetesAdaptiveInvestigationAdapter.xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_5 # type: ignore # mutmut generated
mutants_xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut['xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_6'] = KubernetesAdaptiveInvestigationAdapter.xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_6 # type: ignore # mutmut generated
mutants_xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut['xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_7'] = KubernetesAdaptiveInvestigationAdapter.xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_7 # type: ignore # mutmut generated
mutants_xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut['xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_8'] = KubernetesAdaptiveInvestigationAdapter.xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_8 # type: ignore # mutmut generated
mutants_xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut['xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_9'] = KubernetesAdaptiveInvestigationAdapter.xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_9 # type: ignore # mutmut generated
mutants_xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut['xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_10'] = KubernetesAdaptiveInvestigationAdapter.xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_10 # type: ignore # mutmut generated
mutants_xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut['xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_11'] = KubernetesAdaptiveInvestigationAdapter.xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_11 # type: ignore # mutmut generated
mutants_xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut['xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_12'] = KubernetesAdaptiveInvestigationAdapter.xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_12 # type: ignore # mutmut generated
mutants_xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut['xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_13'] = KubernetesAdaptiveInvestigationAdapter.xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_13 # type: ignore # mutmut generated
mutants_xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut['xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_14'] = KubernetesAdaptiveInvestigationAdapter.xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_14 # type: ignore # mutmut generated
mutants_xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut['xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_15'] = KubernetesAdaptiveInvestigationAdapter.xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_15 # type: ignore # mutmut generated
mutants_xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut['xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_16'] = KubernetesAdaptiveInvestigationAdapter.xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_16 # type: ignore # mutmut generated
mutants_xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut['xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_17'] = KubernetesAdaptiveInvestigationAdapter.xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_17 # type: ignore # mutmut generated
mutants_xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut['xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_18'] = KubernetesAdaptiveInvestigationAdapter.xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_18 # type: ignore # mutmut generated
mutants_xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut['xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_19'] = KubernetesAdaptiveInvestigationAdapter.xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_19 # type: ignore # mutmut generated
mutants_xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut['xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_20'] = KubernetesAdaptiveInvestigationAdapter.xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_20 # type: ignore # mutmut generated
mutants_xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut['xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_21'] = KubernetesAdaptiveInvestigationAdapter.xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_21 # type: ignore # mutmut generated
mutants_xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut['xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_22'] = KubernetesAdaptiveInvestigationAdapter.xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_22 # type: ignore # mutmut generated
mutants_xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut['xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_23'] = KubernetesAdaptiveInvestigationAdapter.xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_23 # type: ignore # mutmut generated
mutants_xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut['xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_24'] = KubernetesAdaptiveInvestigationAdapter.xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_24 # type: ignore # mutmut generated
mutants_xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut['xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_25'] = KubernetesAdaptiveInvestigationAdapter.xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_25 # type: ignore # mutmut generated
mutants_xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut['xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_26'] = KubernetesAdaptiveInvestigationAdapter.xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_26 # type: ignore # mutmut generated
mutants_xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut['xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_27'] = KubernetesAdaptiveInvestigationAdapter.xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_27 # type: ignore # mutmut generated
mutants_xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut['xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_28'] = KubernetesAdaptiveInvestigationAdapter.xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_28 # type: ignore # mutmut generated
mutants_xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut['xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_29'] = KubernetesAdaptiveInvestigationAdapter.xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_29 # type: ignore # mutmut generated
mutants_xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut['xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_30'] = KubernetesAdaptiveInvestigationAdapter.xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_30 # type: ignore # mutmut generated
mutants_xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut['xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_31'] = KubernetesAdaptiveInvestigationAdapter.xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_31 # type: ignore # mutmut generated
mutants_xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut['xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_32'] = KubernetesAdaptiveInvestigationAdapter.xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_32 # type: ignore # mutmut generated
mutants_xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut['xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_33'] = KubernetesAdaptiveInvestigationAdapter.xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_33 # type: ignore # mutmut generated
mutants_xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut['xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_34'] = KubernetesAdaptiveInvestigationAdapter.xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_34 # type: ignore # mutmut generated
mutants_xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut['xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_35'] = KubernetesAdaptiveInvestigationAdapter.xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_35 # type: ignore # mutmut generated
mutants_xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut['xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_36'] = KubernetesAdaptiveInvestigationAdapter.xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_36 # type: ignore # mutmut generated
mutants_xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut['xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_37'] = KubernetesAdaptiveInvestigationAdapter.xǁKubernetesAdaptiveInvestigationAdapterǁinvestigate_resource__mutmut_37 # type: ignore # mutmut generated

mutants_xǁKubernetesAdaptiveInvestigationAdapterǁ_investigate_pod__mutmut['_mutmut_orig'] = KubernetesAdaptiveInvestigationAdapter.xǁKubernetesAdaptiveInvestigationAdapterǁ_investigate_pod__mutmut_orig # type: ignore # mutmut generated
mutants_xǁKubernetesAdaptiveInvestigationAdapterǁ_investigate_pod__mutmut['xǁKubernetesAdaptiveInvestigationAdapterǁ_investigate_pod__mutmut_1'] = KubernetesAdaptiveInvestigationAdapter.xǁKubernetesAdaptiveInvestigationAdapterǁ_investigate_pod__mutmut_1 # type: ignore # mutmut generated
mutants_xǁKubernetesAdaptiveInvestigationAdapterǁ_investigate_pod__mutmut['xǁKubernetesAdaptiveInvestigationAdapterǁ_investigate_pod__mutmut_2'] = KubernetesAdaptiveInvestigationAdapter.xǁKubernetesAdaptiveInvestigationAdapterǁ_investigate_pod__mutmut_2 # type: ignore # mutmut generated
mutants_xǁKubernetesAdaptiveInvestigationAdapterǁ_investigate_pod__mutmut['xǁKubernetesAdaptiveInvestigationAdapterǁ_investigate_pod__mutmut_3'] = KubernetesAdaptiveInvestigationAdapter.xǁKubernetesAdaptiveInvestigationAdapterǁ_investigate_pod__mutmut_3 # type: ignore # mutmut generated
mutants_xǁKubernetesAdaptiveInvestigationAdapterǁ_investigate_pod__mutmut['xǁKubernetesAdaptiveInvestigationAdapterǁ_investigate_pod__mutmut_4'] = KubernetesAdaptiveInvestigationAdapter.xǁKubernetesAdaptiveInvestigationAdapterǁ_investigate_pod__mutmut_4 # type: ignore # mutmut generated
mutants_xǁKubernetesAdaptiveInvestigationAdapterǁ_investigate_pod__mutmut['xǁKubernetesAdaptiveInvestigationAdapterǁ_investigate_pod__mutmut_5'] = KubernetesAdaptiveInvestigationAdapter.xǁKubernetesAdaptiveInvestigationAdapterǁ_investigate_pod__mutmut_5 # type: ignore # mutmut generated
mutants_xǁKubernetesAdaptiveInvestigationAdapterǁ_investigate_pod__mutmut['xǁKubernetesAdaptiveInvestigationAdapterǁ_investigate_pod__mutmut_6'] = KubernetesAdaptiveInvestigationAdapter.xǁKubernetesAdaptiveInvestigationAdapterǁ_investigate_pod__mutmut_6 # type: ignore # mutmut generated
mutants_xǁKubernetesAdaptiveInvestigationAdapterǁ_investigate_pod__mutmut['xǁKubernetesAdaptiveInvestigationAdapterǁ_investigate_pod__mutmut_7'] = KubernetesAdaptiveInvestigationAdapter.xǁKubernetesAdaptiveInvestigationAdapterǁ_investigate_pod__mutmut_7 # type: ignore # mutmut generated
mutants_xǁKubernetesAdaptiveInvestigationAdapterǁ_investigate_pod__mutmut['xǁKubernetesAdaptiveInvestigationAdapterǁ_investigate_pod__mutmut_8'] = KubernetesAdaptiveInvestigationAdapter.xǁKubernetesAdaptiveInvestigationAdapterǁ_investigate_pod__mutmut_8 # type: ignore # mutmut generated
mutants_xǁKubernetesAdaptiveInvestigationAdapterǁ_investigate_pod__mutmut['xǁKubernetesAdaptiveInvestigationAdapterǁ_investigate_pod__mutmut_9'] = KubernetesAdaptiveInvestigationAdapter.xǁKubernetesAdaptiveInvestigationAdapterǁ_investigate_pod__mutmut_9 # type: ignore # mutmut generated
mutants_xǁKubernetesAdaptiveInvestigationAdapterǁ_investigate_pod__mutmut['xǁKubernetesAdaptiveInvestigationAdapterǁ_investigate_pod__mutmut_10'] = KubernetesAdaptiveInvestigationAdapter.xǁKubernetesAdaptiveInvestigationAdapterǁ_investigate_pod__mutmut_10 # type: ignore # mutmut generated
mutants_xǁKubernetesAdaptiveInvestigationAdapterǁ_investigate_pod__mutmut['xǁKubernetesAdaptiveInvestigationAdapterǁ_investigate_pod__mutmut_11'] = KubernetesAdaptiveInvestigationAdapter.xǁKubernetesAdaptiveInvestigationAdapterǁ_investigate_pod__mutmut_11 # type: ignore # mutmut generated
mutants_xǁKubernetesAdaptiveInvestigationAdapterǁ_investigate_pod__mutmut['xǁKubernetesAdaptiveInvestigationAdapterǁ_investigate_pod__mutmut_12'] = KubernetesAdaptiveInvestigationAdapter.xǁKubernetesAdaptiveInvestigationAdapterǁ_investigate_pod__mutmut_12 # type: ignore # mutmut generated
mutants_xǁKubernetesAdaptiveInvestigationAdapterǁ_investigate_pod__mutmut['xǁKubernetesAdaptiveInvestigationAdapterǁ_investigate_pod__mutmut_13'] = KubernetesAdaptiveInvestigationAdapter.xǁKubernetesAdaptiveInvestigationAdapterǁ_investigate_pod__mutmut_13 # type: ignore # mutmut generated
mutants_xǁKubernetesAdaptiveInvestigationAdapterǁ_investigate_pod__mutmut['xǁKubernetesAdaptiveInvestigationAdapterǁ_investigate_pod__mutmut_14'] = KubernetesAdaptiveInvestigationAdapter.xǁKubernetesAdaptiveInvestigationAdapterǁ_investigate_pod__mutmut_14 # type: ignore # mutmut generated
mutants_xǁKubernetesAdaptiveInvestigationAdapterǁ_investigate_pod__mutmut['xǁKubernetesAdaptiveInvestigationAdapterǁ_investigate_pod__mutmut_15'] = KubernetesAdaptiveInvestigationAdapter.xǁKubernetesAdaptiveInvestigationAdapterǁ_investigate_pod__mutmut_15 # type: ignore # mutmut generated
mutants_xǁKubernetesAdaptiveInvestigationAdapterǁ_investigate_pod__mutmut['xǁKubernetesAdaptiveInvestigationAdapterǁ_investigate_pod__mutmut_16'] = KubernetesAdaptiveInvestigationAdapter.xǁKubernetesAdaptiveInvestigationAdapterǁ_investigate_pod__mutmut_16 # type: ignore # mutmut generated
mutants_xǁKubernetesAdaptiveInvestigationAdapterǁ_investigate_pod__mutmut['xǁKubernetesAdaptiveInvestigationAdapterǁ_investigate_pod__mutmut_17'] = KubernetesAdaptiveInvestigationAdapter.xǁKubernetesAdaptiveInvestigationAdapterǁ_investigate_pod__mutmut_17 # type: ignore # mutmut generated
mutants_xǁKubernetesAdaptiveInvestigationAdapterǁ_investigate_pod__mutmut['xǁKubernetesAdaptiveInvestigationAdapterǁ_investigate_pod__mutmut_18'] = KubernetesAdaptiveInvestigationAdapter.xǁKubernetesAdaptiveInvestigationAdapterǁ_investigate_pod__mutmut_18 # type: ignore # mutmut generated
mutants_xǁKubernetesAdaptiveInvestigationAdapterǁ_investigate_pod__mutmut['xǁKubernetesAdaptiveInvestigationAdapterǁ_investigate_pod__mutmut_19'] = KubernetesAdaptiveInvestigationAdapter.xǁKubernetesAdaptiveInvestigationAdapterǁ_investigate_pod__mutmut_19 # type: ignore # mutmut generated
mutants_xǁKubernetesAdaptiveInvestigationAdapterǁ_investigate_pod__mutmut['xǁKubernetesAdaptiveInvestigationAdapterǁ_investigate_pod__mutmut_20'] = KubernetesAdaptiveInvestigationAdapter.xǁKubernetesAdaptiveInvestigationAdapterǁ_investigate_pod__mutmut_20 # type: ignore # mutmut generated

mutants_xǁKubernetesAdaptiveInvestigationAdapterǁ_verify_deployment_exists__mutmut['_mutmut_orig'] = KubernetesAdaptiveInvestigationAdapter.xǁKubernetesAdaptiveInvestigationAdapterǁ_verify_deployment_exists__mutmut_orig # type: ignore # mutmut generated
mutants_xǁKubernetesAdaptiveInvestigationAdapterǁ_verify_deployment_exists__mutmut['xǁKubernetesAdaptiveInvestigationAdapterǁ_verify_deployment_exists__mutmut_1'] = KubernetesAdaptiveInvestigationAdapter.xǁKubernetesAdaptiveInvestigationAdapterǁ_verify_deployment_exists__mutmut_1 # type: ignore # mutmut generated
mutants_xǁKubernetesAdaptiveInvestigationAdapterǁ_verify_deployment_exists__mutmut['xǁKubernetesAdaptiveInvestigationAdapterǁ_verify_deployment_exists__mutmut_2'] = KubernetesAdaptiveInvestigationAdapter.xǁKubernetesAdaptiveInvestigationAdapterǁ_verify_deployment_exists__mutmut_2 # type: ignore # mutmut generated
mutants_xǁKubernetesAdaptiveInvestigationAdapterǁ_verify_deployment_exists__mutmut['xǁKubernetesAdaptiveInvestigationAdapterǁ_verify_deployment_exists__mutmut_3'] = KubernetesAdaptiveInvestigationAdapter.xǁKubernetesAdaptiveInvestigationAdapterǁ_verify_deployment_exists__mutmut_3 # type: ignore # mutmut generated
mutants_xǁKubernetesAdaptiveInvestigationAdapterǁ_verify_deployment_exists__mutmut['xǁKubernetesAdaptiveInvestigationAdapterǁ_verify_deployment_exists__mutmut_4'] = KubernetesAdaptiveInvestigationAdapter.xǁKubernetesAdaptiveInvestigationAdapterǁ_verify_deployment_exists__mutmut_4 # type: ignore # mutmut generated
mutants_xǁKubernetesAdaptiveInvestigationAdapterǁ_verify_deployment_exists__mutmut['xǁKubernetesAdaptiveInvestigationAdapterǁ_verify_deployment_exists__mutmut_5'] = KubernetesAdaptiveInvestigationAdapter.xǁKubernetesAdaptiveInvestigationAdapterǁ_verify_deployment_exists__mutmut_5 # type: ignore # mutmut generated
mutants_xǁKubernetesAdaptiveInvestigationAdapterǁ_verify_deployment_exists__mutmut['xǁKubernetesAdaptiveInvestigationAdapterǁ_verify_deployment_exists__mutmut_6'] = KubernetesAdaptiveInvestigationAdapter.xǁKubernetesAdaptiveInvestigationAdapterǁ_verify_deployment_exists__mutmut_6 # type: ignore # mutmut generated
mutants_xǁKubernetesAdaptiveInvestigationAdapterǁ_verify_deployment_exists__mutmut['xǁKubernetesAdaptiveInvestigationAdapterǁ_verify_deployment_exists__mutmut_7'] = KubernetesAdaptiveInvestigationAdapter.xǁKubernetesAdaptiveInvestigationAdapterǁ_verify_deployment_exists__mutmut_7 # type: ignore # mutmut generated
mutants_xǁKubernetesAdaptiveInvestigationAdapterǁ_verify_deployment_exists__mutmut['xǁKubernetesAdaptiveInvestigationAdapterǁ_verify_deployment_exists__mutmut_8'] = KubernetesAdaptiveInvestigationAdapter.xǁKubernetesAdaptiveInvestigationAdapterǁ_verify_deployment_exists__mutmut_8 # type: ignore # mutmut generated
mutants_xǁKubernetesAdaptiveInvestigationAdapterǁ_verify_deployment_exists__mutmut['xǁKubernetesAdaptiveInvestigationAdapterǁ_verify_deployment_exists__mutmut_9'] = KubernetesAdaptiveInvestigationAdapter.xǁKubernetesAdaptiveInvestigationAdapterǁ_verify_deployment_exists__mutmut_9 # type: ignore # mutmut generated
mutants_xǁKubernetesAdaptiveInvestigationAdapterǁ_verify_deployment_exists__mutmut['xǁKubernetesAdaptiveInvestigationAdapterǁ_verify_deployment_exists__mutmut_10'] = KubernetesAdaptiveInvestigationAdapter.xǁKubernetesAdaptiveInvestigationAdapterǁ_verify_deployment_exists__mutmut_10 # type: ignore # mutmut generated
mutants_xǁKubernetesAdaptiveInvestigationAdapterǁ_verify_deployment_exists__mutmut['xǁKubernetesAdaptiveInvestigationAdapterǁ_verify_deployment_exists__mutmut_11'] = KubernetesAdaptiveInvestigationAdapter.xǁKubernetesAdaptiveInvestigationAdapterǁ_verify_deployment_exists__mutmut_11 # type: ignore # mutmut generated

mutants_xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_events__mutmut['_mutmut_orig'] = KubernetesAdaptiveInvestigationAdapter.xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_events__mutmut_orig # type: ignore # mutmut generated
mutants_xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_events__mutmut['xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_events__mutmut_1'] = KubernetesAdaptiveInvestigationAdapter.xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_events__mutmut_1 # type: ignore # mutmut generated
mutants_xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_events__mutmut['xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_events__mutmut_2'] = KubernetesAdaptiveInvestigationAdapter.xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_events__mutmut_2 # type: ignore # mutmut generated
mutants_xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_events__mutmut['xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_events__mutmut_3'] = KubernetesAdaptiveInvestigationAdapter.xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_events__mutmut_3 # type: ignore # mutmut generated
mutants_xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_events__mutmut['xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_events__mutmut_4'] = KubernetesAdaptiveInvestigationAdapter.xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_events__mutmut_4 # type: ignore # mutmut generated
mutants_xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_events__mutmut['xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_events__mutmut_5'] = KubernetesAdaptiveInvestigationAdapter.xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_events__mutmut_5 # type: ignore # mutmut generated
mutants_xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_events__mutmut['xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_events__mutmut_6'] = KubernetesAdaptiveInvestigationAdapter.xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_events__mutmut_6 # type: ignore # mutmut generated
mutants_xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_events__mutmut['xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_events__mutmut_7'] = KubernetesAdaptiveInvestigationAdapter.xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_events__mutmut_7 # type: ignore # mutmut generated
mutants_xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_events__mutmut['xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_events__mutmut_8'] = KubernetesAdaptiveInvestigationAdapter.xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_events__mutmut_8 # type: ignore # mutmut generated
mutants_xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_events__mutmut['xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_events__mutmut_9'] = KubernetesAdaptiveInvestigationAdapter.xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_events__mutmut_9 # type: ignore # mutmut generated
mutants_xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_events__mutmut['xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_events__mutmut_10'] = KubernetesAdaptiveInvestigationAdapter.xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_events__mutmut_10 # type: ignore # mutmut generated
mutants_xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_events__mutmut['xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_events__mutmut_11'] = KubernetesAdaptiveInvestigationAdapter.xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_events__mutmut_11 # type: ignore # mutmut generated
mutants_xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_events__mutmut['xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_events__mutmut_12'] = KubernetesAdaptiveInvestigationAdapter.xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_events__mutmut_12 # type: ignore # mutmut generated
mutants_xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_events__mutmut['xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_events__mutmut_13'] = KubernetesAdaptiveInvestigationAdapter.xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_events__mutmut_13 # type: ignore # mutmut generated

mutants_xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_logs__mutmut['_mutmut_orig'] = KubernetesAdaptiveInvestigationAdapter.xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_logs__mutmut_orig # type: ignore # mutmut generated
mutants_xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_logs__mutmut['xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_logs__mutmut_1'] = KubernetesAdaptiveInvestigationAdapter.xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_logs__mutmut_1 # type: ignore # mutmut generated
mutants_xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_logs__mutmut['xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_logs__mutmut_2'] = KubernetesAdaptiveInvestigationAdapter.xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_logs__mutmut_2 # type: ignore # mutmut generated
mutants_xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_logs__mutmut['xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_logs__mutmut_3'] = KubernetesAdaptiveInvestigationAdapter.xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_logs__mutmut_3 # type: ignore # mutmut generated
mutants_xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_logs__mutmut['xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_logs__mutmut_4'] = KubernetesAdaptiveInvestigationAdapter.xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_logs__mutmut_4 # type: ignore # mutmut generated
mutants_xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_logs__mutmut['xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_logs__mutmut_5'] = KubernetesAdaptiveInvestigationAdapter.xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_logs__mutmut_5 # type: ignore # mutmut generated
mutants_xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_logs__mutmut['xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_logs__mutmut_6'] = KubernetesAdaptiveInvestigationAdapter.xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_logs__mutmut_6 # type: ignore # mutmut generated
mutants_xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_logs__mutmut['xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_logs__mutmut_7'] = KubernetesAdaptiveInvestigationAdapter.xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_logs__mutmut_7 # type: ignore # mutmut generated
mutants_xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_logs__mutmut['xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_logs__mutmut_8'] = KubernetesAdaptiveInvestigationAdapter.xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_logs__mutmut_8 # type: ignore # mutmut generated
mutants_xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_logs__mutmut['xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_logs__mutmut_9'] = KubernetesAdaptiveInvestigationAdapter.xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_logs__mutmut_9 # type: ignore # mutmut generated
mutants_xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_logs__mutmut['xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_logs__mutmut_10'] = KubernetesAdaptiveInvestigationAdapter.xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_logs__mutmut_10 # type: ignore # mutmut generated
mutants_xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_logs__mutmut['xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_logs__mutmut_11'] = KubernetesAdaptiveInvestigationAdapter.xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_logs__mutmut_11 # type: ignore # mutmut generated
mutants_xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_logs__mutmut['xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_logs__mutmut_12'] = KubernetesAdaptiveInvestigationAdapter.xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_logs__mutmut_12 # type: ignore # mutmut generated
mutants_xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_logs__mutmut['xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_logs__mutmut_13'] = KubernetesAdaptiveInvestigationAdapter.xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_logs__mutmut_13 # type: ignore # mutmut generated
mutants_xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_logs__mutmut['xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_logs__mutmut_14'] = KubernetesAdaptiveInvestigationAdapter.xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_logs__mutmut_14 # type: ignore # mutmut generated
mutants_xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_logs__mutmut['xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_logs__mutmut_15'] = KubernetesAdaptiveInvestigationAdapter.xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_logs__mutmut_15 # type: ignore # mutmut generated
mutants_xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_logs__mutmut['xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_logs__mutmut_16'] = KubernetesAdaptiveInvestigationAdapter.xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_logs__mutmut_16 # type: ignore # mutmut generated
mutants_xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_logs__mutmut['xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_logs__mutmut_17'] = KubernetesAdaptiveInvestigationAdapter.xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_logs__mutmut_17 # type: ignore # mutmut generated
mutants_xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_logs__mutmut['xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_logs__mutmut_18'] = KubernetesAdaptiveInvestigationAdapter.xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_logs__mutmut_18 # type: ignore # mutmut generated
mutants_xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_logs__mutmut['xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_logs__mutmut_19'] = KubernetesAdaptiveInvestigationAdapter.xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_logs__mutmut_19 # type: ignore # mutmut generated
mutants_xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_logs__mutmut['xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_logs__mutmut_20'] = KubernetesAdaptiveInvestigationAdapter.xǁKubernetesAdaptiveInvestigationAdapterǁ_fetch_logs__mutmut_20 # type: ignore # mutmut generated
mutants_x__extract_container_status__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__extract_container_status__mutmut)
def _extract_container_status(pod: object) -> tuple[int, str | None]:
    statuses = pod.status.container_statuses or []  # type: ignore[attr-defined]
    restart_count = sum(status.restart_count or 0 for status in statuses)

    last_termination_reason = None
    for status in statuses:
        terminated = status.last_state.terminated
        if terminated is not None and terminated.reason:
            last_termination_reason = terminated.reason
            break

    return restart_count, last_termination_reason


def x__extract_container_status__mutmut_orig(pod: object) -> tuple[int, str | None]:
    statuses = pod.status.container_statuses or []  # type: ignore[attr-defined]
    restart_count = sum(status.restart_count or 0 for status in statuses)

    last_termination_reason = None
    for status in statuses:
        terminated = status.last_state.terminated
        if terminated is not None and terminated.reason:
            last_termination_reason = terminated.reason
            break

    return restart_count, last_termination_reason


def x__extract_container_status__mutmut_1(pod: object) -> tuple[int, str | None]:
    statuses = None  # type: ignore[attr-defined]
    restart_count = sum(status.restart_count or 0 for status in statuses)

    last_termination_reason = None
    for status in statuses:
        terminated = status.last_state.terminated
        if terminated is not None and terminated.reason:
            last_termination_reason = terminated.reason
            break

    return restart_count, last_termination_reason


def x__extract_container_status__mutmut_2(pod: object) -> tuple[int, str | None]:
    statuses = pod.status.container_statuses and []  # type: ignore[attr-defined]
    restart_count = sum(status.restart_count or 0 for status in statuses)

    last_termination_reason = None
    for status in statuses:
        terminated = status.last_state.terminated
        if terminated is not None and terminated.reason:
            last_termination_reason = terminated.reason
            break

    return restart_count, last_termination_reason


def x__extract_container_status__mutmut_3(pod: object) -> tuple[int, str | None]:
    statuses = pod.status.container_statuses or []  # type: ignore[attr-defined]
    restart_count = None

    last_termination_reason = None
    for status in statuses:
        terminated = status.last_state.terminated
        if terminated is not None and terminated.reason:
            last_termination_reason = terminated.reason
            break

    return restart_count, last_termination_reason


def x__extract_container_status__mutmut_4(pod: object) -> tuple[int, str | None]:
    statuses = pod.status.container_statuses or []  # type: ignore[attr-defined]
    restart_count = sum(None)

    last_termination_reason = None
    for status in statuses:
        terminated = status.last_state.terminated
        if terminated is not None and terminated.reason:
            last_termination_reason = terminated.reason
            break

    return restart_count, last_termination_reason


def x__extract_container_status__mutmut_5(pod: object) -> tuple[int, str | None]:
    statuses = pod.status.container_statuses or []  # type: ignore[attr-defined]
    restart_count = sum(status.restart_count and 0 for status in statuses)

    last_termination_reason = None
    for status in statuses:
        terminated = status.last_state.terminated
        if terminated is not None and terminated.reason:
            last_termination_reason = terminated.reason
            break

    return restart_count, last_termination_reason


def x__extract_container_status__mutmut_6(pod: object) -> tuple[int, str | None]:
    statuses = pod.status.container_statuses or []  # type: ignore[attr-defined]
    restart_count = sum(status.restart_count or 1 for status in statuses)

    last_termination_reason = None
    for status in statuses:
        terminated = status.last_state.terminated
        if terminated is not None and terminated.reason:
            last_termination_reason = terminated.reason
            break

    return restart_count, last_termination_reason


def x__extract_container_status__mutmut_7(pod: object) -> tuple[int, str | None]:
    statuses = pod.status.container_statuses or []  # type: ignore[attr-defined]
    restart_count = sum(status.restart_count or 0 for status in statuses)

    last_termination_reason = ""
    for status in statuses:
        terminated = status.last_state.terminated
        if terminated is not None and terminated.reason:
            last_termination_reason = terminated.reason
            break

    return restart_count, last_termination_reason


def x__extract_container_status__mutmut_8(pod: object) -> tuple[int, str | None]:
    statuses = pod.status.container_statuses or []  # type: ignore[attr-defined]
    restart_count = sum(status.restart_count or 0 for status in statuses)

    last_termination_reason = None
    for status in statuses:
        terminated = None
        if terminated is not None and terminated.reason:
            last_termination_reason = terminated.reason
            break

    return restart_count, last_termination_reason


def x__extract_container_status__mutmut_9(pod: object) -> tuple[int, str | None]:
    statuses = pod.status.container_statuses or []  # type: ignore[attr-defined]
    restart_count = sum(status.restart_count or 0 for status in statuses)

    last_termination_reason = None
    for status in statuses:
        terminated = status.last_state.terminated
        if terminated is not None or terminated.reason:
            last_termination_reason = terminated.reason
            break

    return restart_count, last_termination_reason


def x__extract_container_status__mutmut_10(pod: object) -> tuple[int, str | None]:
    statuses = pod.status.container_statuses or []  # type: ignore[attr-defined]
    restart_count = sum(status.restart_count or 0 for status in statuses)

    last_termination_reason = None
    for status in statuses:
        terminated = status.last_state.terminated
        if terminated is None and terminated.reason:
            last_termination_reason = terminated.reason
            break

    return restart_count, last_termination_reason


def x__extract_container_status__mutmut_11(pod: object) -> tuple[int, str | None]:
    statuses = pod.status.container_statuses or []  # type: ignore[attr-defined]
    restart_count = sum(status.restart_count or 0 for status in statuses)

    last_termination_reason = None
    for status in statuses:
        terminated = status.last_state.terminated
        if terminated is not None and terminated.reason:
            last_termination_reason = None
            break

    return restart_count, last_termination_reason


def x__extract_container_status__mutmut_12(pod: object) -> tuple[int, str | None]:
    statuses = pod.status.container_statuses or []  # type: ignore[attr-defined]
    restart_count = sum(status.restart_count or 0 for status in statuses)

    last_termination_reason = None
    for status in statuses:
        terminated = status.last_state.terminated
        if terminated is not None and terminated.reason:
            last_termination_reason = terminated.reason
            return

    return restart_count, last_termination_reason

mutants_x__extract_container_status__mutmut['_mutmut_orig'] = x__extract_container_status__mutmut_orig # type: ignore # mutmut generated
mutants_x__extract_container_status__mutmut['x__extract_container_status__mutmut_1'] = x__extract_container_status__mutmut_1 # type: ignore # mutmut generated
mutants_x__extract_container_status__mutmut['x__extract_container_status__mutmut_2'] = x__extract_container_status__mutmut_2 # type: ignore # mutmut generated
mutants_x__extract_container_status__mutmut['x__extract_container_status__mutmut_3'] = x__extract_container_status__mutmut_3 # type: ignore # mutmut generated
mutants_x__extract_container_status__mutmut['x__extract_container_status__mutmut_4'] = x__extract_container_status__mutmut_4 # type: ignore # mutmut generated
mutants_x__extract_container_status__mutmut['x__extract_container_status__mutmut_5'] = x__extract_container_status__mutmut_5 # type: ignore # mutmut generated
mutants_x__extract_container_status__mutmut['x__extract_container_status__mutmut_6'] = x__extract_container_status__mutmut_6 # type: ignore # mutmut generated
mutants_x__extract_container_status__mutmut['x__extract_container_status__mutmut_7'] = x__extract_container_status__mutmut_7 # type: ignore # mutmut generated
mutants_x__extract_container_status__mutmut['x__extract_container_status__mutmut_8'] = x__extract_container_status__mutmut_8 # type: ignore # mutmut generated
mutants_x__extract_container_status__mutmut['x__extract_container_status__mutmut_9'] = x__extract_container_status__mutmut_9 # type: ignore # mutmut generated
mutants_x__extract_container_status__mutmut['x__extract_container_status__mutmut_10'] = x__extract_container_status__mutmut_10 # type: ignore # mutmut generated
mutants_x__extract_container_status__mutmut['x__extract_container_status__mutmut_11'] = x__extract_container_status__mutmut_11 # type: ignore # mutmut generated
mutants_x__extract_container_status__mutmut['x__extract_container_status__mutmut_12'] = x__extract_container_status__mutmut_12 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__translate_error__mutmut)
def _translate_error(exc: Exception, namespace: str, name: str) -> Exception:
    status = getattr(exc, "status", None)
    context = {"namespace": namespace, "name": name}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(
            f"Resource {name!r} not found in namespace {namespace!r}", context=context
        )
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to resource {name!r} in namespace {namespace!r}", context=context
        )
    return ClusterUnreachableError(f"Cannot investigate resource {name!r}: {exc}")


def x__translate_error__mutmut_orig(exc: Exception, namespace: str, name: str) -> Exception:
    status = getattr(exc, "status", None)
    context = {"namespace": namespace, "name": name}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(
            f"Resource {name!r} not found in namespace {namespace!r}", context=context
        )
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to resource {name!r} in namespace {namespace!r}", context=context
        )
    return ClusterUnreachableError(f"Cannot investigate resource {name!r}: {exc}")


def x__translate_error__mutmut_1(exc: Exception, namespace: str, name: str) -> Exception:
    status = None
    context = {"namespace": namespace, "name": name}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(
            f"Resource {name!r} not found in namespace {namespace!r}", context=context
        )
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to resource {name!r} in namespace {namespace!r}", context=context
        )
    return ClusterUnreachableError(f"Cannot investigate resource {name!r}: {exc}")


def x__translate_error__mutmut_2(exc: Exception, namespace: str, name: str) -> Exception:
    status = getattr(None, "status", None)
    context = {"namespace": namespace, "name": name}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(
            f"Resource {name!r} not found in namespace {namespace!r}", context=context
        )
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to resource {name!r} in namespace {namespace!r}", context=context
        )
    return ClusterUnreachableError(f"Cannot investigate resource {name!r}: {exc}")


def x__translate_error__mutmut_3(exc: Exception, namespace: str, name: str) -> Exception:
    status = getattr(exc, None, None)
    context = {"namespace": namespace, "name": name}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(
            f"Resource {name!r} not found in namespace {namespace!r}", context=context
        )
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to resource {name!r} in namespace {namespace!r}", context=context
        )
    return ClusterUnreachableError(f"Cannot investigate resource {name!r}: {exc}")


def x__translate_error__mutmut_4(exc: Exception, namespace: str, name: str) -> Exception:
    status = getattr("status", None)
    context = {"namespace": namespace, "name": name}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(
            f"Resource {name!r} not found in namespace {namespace!r}", context=context
        )
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to resource {name!r} in namespace {namespace!r}", context=context
        )
    return ClusterUnreachableError(f"Cannot investigate resource {name!r}: {exc}")


def x__translate_error__mutmut_5(exc: Exception, namespace: str, name: str) -> Exception:
    status = getattr(exc, None)
    context = {"namespace": namespace, "name": name}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(
            f"Resource {name!r} not found in namespace {namespace!r}", context=context
        )
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to resource {name!r} in namespace {namespace!r}", context=context
        )
    return ClusterUnreachableError(f"Cannot investigate resource {name!r}: {exc}")


def x__translate_error__mutmut_6(exc: Exception, namespace: str, name: str) -> Exception:
    status = getattr(exc, "status", )
    context = {"namespace": namespace, "name": name}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(
            f"Resource {name!r} not found in namespace {namespace!r}", context=context
        )
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to resource {name!r} in namespace {namespace!r}", context=context
        )
    return ClusterUnreachableError(f"Cannot investigate resource {name!r}: {exc}")


def x__translate_error__mutmut_7(exc: Exception, namespace: str, name: str) -> Exception:
    status = getattr(exc, "XXstatusXX", None)
    context = {"namespace": namespace, "name": name}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(
            f"Resource {name!r} not found in namespace {namespace!r}", context=context
        )
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to resource {name!r} in namespace {namespace!r}", context=context
        )
    return ClusterUnreachableError(f"Cannot investigate resource {name!r}: {exc}")


def x__translate_error__mutmut_8(exc: Exception, namespace: str, name: str) -> Exception:
    status = getattr(exc, "STATUS", None)
    context = {"namespace": namespace, "name": name}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(
            f"Resource {name!r} not found in namespace {namespace!r}", context=context
        )
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to resource {name!r} in namespace {namespace!r}", context=context
        )
    return ClusterUnreachableError(f"Cannot investigate resource {name!r}: {exc}")


def x__translate_error__mutmut_9(exc: Exception, namespace: str, name: str) -> Exception:
    status = getattr(exc, "status", None)
    context = None
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(
            f"Resource {name!r} not found in namespace {namespace!r}", context=context
        )
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to resource {name!r} in namespace {namespace!r}", context=context
        )
    return ClusterUnreachableError(f"Cannot investigate resource {name!r}: {exc}")


def x__translate_error__mutmut_10(exc: Exception, namespace: str, name: str) -> Exception:
    status = getattr(exc, "status", None)
    context = {"XXnamespaceXX": namespace, "name": name}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(
            f"Resource {name!r} not found in namespace {namespace!r}", context=context
        )
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to resource {name!r} in namespace {namespace!r}", context=context
        )
    return ClusterUnreachableError(f"Cannot investigate resource {name!r}: {exc}")


def x__translate_error__mutmut_11(exc: Exception, namespace: str, name: str) -> Exception:
    status = getattr(exc, "status", None)
    context = {"NAMESPACE": namespace, "name": name}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(
            f"Resource {name!r} not found in namespace {namespace!r}", context=context
        )
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to resource {name!r} in namespace {namespace!r}", context=context
        )
    return ClusterUnreachableError(f"Cannot investigate resource {name!r}: {exc}")


def x__translate_error__mutmut_12(exc: Exception, namespace: str, name: str) -> Exception:
    status = getattr(exc, "status", None)
    context = {"namespace": namespace, "XXnameXX": name}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(
            f"Resource {name!r} not found in namespace {namespace!r}", context=context
        )
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to resource {name!r} in namespace {namespace!r}", context=context
        )
    return ClusterUnreachableError(f"Cannot investigate resource {name!r}: {exc}")


def x__translate_error__mutmut_13(exc: Exception, namespace: str, name: str) -> Exception:
    status = getattr(exc, "status", None)
    context = {"namespace": namespace, "NAME": name}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(
            f"Resource {name!r} not found in namespace {namespace!r}", context=context
        )
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to resource {name!r} in namespace {namespace!r}", context=context
        )
    return ClusterUnreachableError(f"Cannot investigate resource {name!r}: {exc}")


def x__translate_error__mutmut_14(exc: Exception, namespace: str, name: str) -> Exception:
    status = getattr(exc, "status", None)
    context = {"namespace": namespace, "name": name}
    if status != _K8S_NOT_FOUND:
        return ResourceNotFoundError(
            f"Resource {name!r} not found in namespace {namespace!r}", context=context
        )
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to resource {name!r} in namespace {namespace!r}", context=context
        )
    return ClusterUnreachableError(f"Cannot investigate resource {name!r}: {exc}")


def x__translate_error__mutmut_15(exc: Exception, namespace: str, name: str) -> Exception:
    status = getattr(exc, "status", None)
    context = {"namespace": namespace, "name": name}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(
            None, context=context
        )
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to resource {name!r} in namespace {namespace!r}", context=context
        )
    return ClusterUnreachableError(f"Cannot investigate resource {name!r}: {exc}")


def x__translate_error__mutmut_16(exc: Exception, namespace: str, name: str) -> Exception:
    status = getattr(exc, "status", None)
    context = {"namespace": namespace, "name": name}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(
            f"Resource {name!r} not found in namespace {namespace!r}", context=None
        )
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to resource {name!r} in namespace {namespace!r}", context=context
        )
    return ClusterUnreachableError(f"Cannot investigate resource {name!r}: {exc}")


def x__translate_error__mutmut_17(exc: Exception, namespace: str, name: str) -> Exception:
    status = getattr(exc, "status", None)
    context = {"namespace": namespace, "name": name}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(
            context=context
        )
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to resource {name!r} in namespace {namespace!r}", context=context
        )
    return ClusterUnreachableError(f"Cannot investigate resource {name!r}: {exc}")


def x__translate_error__mutmut_18(exc: Exception, namespace: str, name: str) -> Exception:
    status = getattr(exc, "status", None)
    context = {"namespace": namespace, "name": name}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(
            f"Resource {name!r} not found in namespace {namespace!r}", )
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to resource {name!r} in namespace {namespace!r}", context=context
        )
    return ClusterUnreachableError(f"Cannot investigate resource {name!r}: {exc}")


def x__translate_error__mutmut_19(exc: Exception, namespace: str, name: str) -> Exception:
    status = getattr(exc, "status", None)
    context = {"namespace": namespace, "name": name}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(
            f"Resource {name!r} not found in namespace {namespace!r}", context=context
        )
    if status != _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to resource {name!r} in namespace {namespace!r}", context=context
        )
    return ClusterUnreachableError(f"Cannot investigate resource {name!r}: {exc}")


def x__translate_error__mutmut_20(exc: Exception, namespace: str, name: str) -> Exception:
    status = getattr(exc, "status", None)
    context = {"namespace": namespace, "name": name}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(
            f"Resource {name!r} not found in namespace {namespace!r}", context=context
        )
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            None, context=context
        )
    return ClusterUnreachableError(f"Cannot investigate resource {name!r}: {exc}")


def x__translate_error__mutmut_21(exc: Exception, namespace: str, name: str) -> Exception:
    status = getattr(exc, "status", None)
    context = {"namespace": namespace, "name": name}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(
            f"Resource {name!r} not found in namespace {namespace!r}", context=context
        )
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to resource {name!r} in namespace {namespace!r}", context=None
        )
    return ClusterUnreachableError(f"Cannot investigate resource {name!r}: {exc}")


def x__translate_error__mutmut_22(exc: Exception, namespace: str, name: str) -> Exception:
    status = getattr(exc, "status", None)
    context = {"namespace": namespace, "name": name}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(
            f"Resource {name!r} not found in namespace {namespace!r}", context=context
        )
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            context=context
        )
    return ClusterUnreachableError(f"Cannot investigate resource {name!r}: {exc}")


def x__translate_error__mutmut_23(exc: Exception, namespace: str, name: str) -> Exception:
    status = getattr(exc, "status", None)
    context = {"namespace": namespace, "name": name}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(
            f"Resource {name!r} not found in namespace {namespace!r}", context=context
        )
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to resource {name!r} in namespace {namespace!r}", )
    return ClusterUnreachableError(f"Cannot investigate resource {name!r}: {exc}")


def x__translate_error__mutmut_24(exc: Exception, namespace: str, name: str) -> Exception:
    status = getattr(exc, "status", None)
    context = {"namespace": namespace, "name": name}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(
            f"Resource {name!r} not found in namespace {namespace!r}", context=context
        )
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to resource {name!r} in namespace {namespace!r}", context=context
        )
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
mutants_x__translate_error__mutmut['x__translate_error__mutmut_15'] = x__translate_error__mutmut_15 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_16'] = x__translate_error__mutmut_16 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_17'] = x__translate_error__mutmut_17 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_18'] = x__translate_error__mutmut_18 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_19'] = x__translate_error__mutmut_19 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_20'] = x__translate_error__mutmut_20 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_21'] = x__translate_error__mutmut_21 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_22'] = x__translate_error__mutmut_22 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_23'] = x__translate_error__mutmut_23 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_24'] = x__translate_error__mutmut_24 # type: ignore # mutmut generated
