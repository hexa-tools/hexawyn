from __future__ import annotations

_DAEMONSET_OWNER_KIND = "DaemonSet"


def is_known_system_daemonset(
    owner_kind: str | None, pod_name: str, known_name_fragments: tuple[str, ...]
) -> bool:
    if owner_kind != _DAEMONSET_OWNER_KIND:
        return False
    return any(fragment in pod_name for fragment in known_name_fragments)
