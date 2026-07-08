from abc import ABC, abstractmethod
from typing import TypedDict


class PatchFieldRawData(TypedDict):
    field_path: str
    resource: str
    value: str
    source_file: str
    patch_type: str
    order: int


class BaseFieldRawData(TypedDict):
    field_path: str
    resource: str
    value: str


class KustomizePatchAnalysisPort(ABC):
    @abstractmethod
    def extract_patch_fields(self, overlay_path: str) -> list[PatchFieldRawData]: ...

    @abstractmethod
    def extract_base_fields(self, overlay_path: str) -> list[BaseFieldRawData]: ...
