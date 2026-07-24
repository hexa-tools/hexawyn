from dataclasses import dataclass


@dataclass(frozen=True)
class ServiceDependencyGraphCommand:
    namespace: str | None = None
