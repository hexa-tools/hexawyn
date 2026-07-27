from __future__ import annotations

from hexawyn.domain.models.pod_security import ViolationType

_FIXES: dict[ViolationType, str] = {
    "privileged": "Set privileged: false in the container's securityContext.",
    "host_pid": "Set hostPID: false in the pod spec (unless this is a legitimate system DaemonSet).",  # noqa: E501
    "host_network": "Set hostNetwork: false in the pod spec.",
    "host_ipc": "Set hostIPC: false in the pod spec.",
    "run_as_root": "Set runAsNonRoot: true (and a non-zero runAsUser) in the securityContext.",
    "allow_privilege_escalation": "Set allowPrivilegeEscalation: false in the container's securityContext.",  # noqa: E501
}


def recommend_fix(violation_type: ViolationType, capability: str | None = None) -> str:
    if violation_type == "dangerous_capability":
        return (
            f"Remove the '{capability}' capability from securityContext.capabilities.add "
            "(drop ALL and add back only what's required)."
        )
    return _FIXES[violation_type]
