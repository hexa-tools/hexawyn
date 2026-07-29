from dataclasses import dataclass, field


@dataclass
class UnintendedExternalExposureResponse:
    namespace: str = ""
    total_services: int = 0
    findings: list[dict[str, object]] = field(default_factory=list)
    error: str | None = None
