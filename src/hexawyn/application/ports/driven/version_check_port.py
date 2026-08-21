from abc import ABC, abstractmethod


class VersionCheckPort(ABC):
    @abstractmethod
    def fetch_latest_version(self) -> str:
        """Return the latest published hexawyn version, or "" when unavailable."""
