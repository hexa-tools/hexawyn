from dataclasses import dataclass, field


@dataclass(frozen=True)
class CalicoSegmentationAuditCommand:
    """Optional namespace filter and excluded namespaces for the audit."""

    namespace: str | None = None
    excluded_namespaces: tuple[str, ...] = field(default_factory=tuple)
