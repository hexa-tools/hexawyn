from dataclasses import dataclass


@dataclass(frozen=True)
class ScanContainerVulnerabilitiesCommand:
    namespace: str | None = None
    namespaces: list[str] | None = None
