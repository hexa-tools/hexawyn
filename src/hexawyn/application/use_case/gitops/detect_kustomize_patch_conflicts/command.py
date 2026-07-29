from dataclasses import dataclass


@dataclass(frozen=True)
class DetectKustomizePatchConflictsCommand:
    namespace: str | None = None
    overlay_path: str = ""
