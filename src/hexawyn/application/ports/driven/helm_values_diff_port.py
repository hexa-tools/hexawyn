from abc import ABC, abstractmethod
from typing import TypedDict


class HelmReleaseValues(TypedDict):
    release: str
    namespace: str
    values: dict[str, object]


class HelmValuesDiffPort(ABC):
    """Driven port — retrieves the effective Helm values for a release.

    "Effective" means the merged, user-supplied values as returned by
    ``helm get values <release> -n <namespace> -a`` (chart defaults plus any
    ``--set`` overrides applied at install/upgrade time) — never the raw
    values.yaml file, which would miss CI overrides.
    """

    @abstractmethod
    def get_effective_values(self, release: str, namespace: str) -> HelmReleaseValues:
        """Return the effective values for *release* in *namespace*.

        Raises ComponentNotInstalledError when the helm CLI is unavailable.
        Raises ManifestRenderError when the release does not exist or helm fails.
        """
