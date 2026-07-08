import subprocess

PROVIDERS: dict[str, tuple[str, str]] = {
    "aws": ("AWS EKS + CloudWatch", "hexawyn[aws]"),
    "azure": ("Azure AKS + Azure Monitor", "hexawyn[azure]"),
    "gcp": ("GCP GKE + Cloud Operations", "hexawyn[gcp]"),
    "openshift": ("Red Hat OpenShift", "hexawyn[openshift]"),
    "datadog": ("Datadog", "hexawyn[datadog]"),
}


def install_selected_providers(selected: list[str] | None) -> None:
    """
    Install selected provider extras via pip after user choice in SetupWizard.
    Called from SetupWizardScreen step 2 when user clicks 'Install Selected'.
    Does nothing if selected is empty (vanilla only).
    """
    if not selected:
        return
    extras = ",".join(selected)
    package = f"hexawyn[{extras}]"
    subprocess.run(["pip", "install", package], check=True)
