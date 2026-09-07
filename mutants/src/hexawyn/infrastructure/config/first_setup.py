import subprocess

PROVIDERS: dict[str, tuple[str, str]] = {
    "aws": ("AWS EKS + CloudWatch", "hexawyn[aws]"),
    "azure": ("Azure AKS + Azure Monitor", "hexawyn[azure]"),
    "gcp": ("GCP GKE + Cloud Operations", "hexawyn[gcp]"),
    "openshift": ("Red Hat OpenShift", "hexawyn[openshift]"),
    "datadog": ("Datadog", "hexawyn[datadog]"),
}


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_install_selected_providers__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_install_selected_providers__mutmut)
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


def x_install_selected_providers__mutmut_orig(selected: list[str] | None) -> None:
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


def x_install_selected_providers__mutmut_1(selected: list[str] | None) -> None:
    """
    Install selected provider extras via pip after user choice in SetupWizard.
    Called from SetupWizardScreen step 2 when user clicks 'Install Selected'.
    Does nothing if selected is empty (vanilla only).
    """
    if selected:
        return
    extras = ",".join(selected)
    package = f"hexawyn[{extras}]"
    subprocess.run(["pip", "install", package], check=True)


def x_install_selected_providers__mutmut_2(selected: list[str] | None) -> None:
    """
    Install selected provider extras via pip after user choice in SetupWizard.
    Called from SetupWizardScreen step 2 when user clicks 'Install Selected'.
    Does nothing if selected is empty (vanilla only).
    """
    if not selected:
        return
    extras = None
    package = f"hexawyn[{extras}]"
    subprocess.run(["pip", "install", package], check=True)


def x_install_selected_providers__mutmut_3(selected: list[str] | None) -> None:
    """
    Install selected provider extras via pip after user choice in SetupWizard.
    Called from SetupWizardScreen step 2 when user clicks 'Install Selected'.
    Does nothing if selected is empty (vanilla only).
    """
    if not selected:
        return
    extras = ",".join(None)
    package = f"hexawyn[{extras}]"
    subprocess.run(["pip", "install", package], check=True)


def x_install_selected_providers__mutmut_4(selected: list[str] | None) -> None:
    """
    Install selected provider extras via pip after user choice in SetupWizard.
    Called from SetupWizardScreen step 2 when user clicks 'Install Selected'.
    Does nothing if selected is empty (vanilla only).
    """
    if not selected:
        return
    extras = "XX,XX".join(selected)
    package = f"hexawyn[{extras}]"
    subprocess.run(["pip", "install", package], check=True)


def x_install_selected_providers__mutmut_5(selected: list[str] | None) -> None:
    """
    Install selected provider extras via pip after user choice in SetupWizard.
    Called from SetupWizardScreen step 2 when user clicks 'Install Selected'.
    Does nothing if selected is empty (vanilla only).
    """
    if not selected:
        return
    extras = ",".join(selected)
    package = None
    subprocess.run(["pip", "install", package], check=True)


def x_install_selected_providers__mutmut_6(selected: list[str] | None) -> None:
    """
    Install selected provider extras via pip after user choice in SetupWizard.
    Called from SetupWizardScreen step 2 when user clicks 'Install Selected'.
    Does nothing if selected is empty (vanilla only).
    """
    if not selected:
        return
    extras = ",".join(selected)
    package = f"hexawyn[{extras}]"
    subprocess.run(None, check=True)


def x_install_selected_providers__mutmut_7(selected: list[str] | None) -> None:
    """
    Install selected provider extras via pip after user choice in SetupWizard.
    Called from SetupWizardScreen step 2 when user clicks 'Install Selected'.
    Does nothing if selected is empty (vanilla only).
    """
    if not selected:
        return
    extras = ",".join(selected)
    package = f"hexawyn[{extras}]"
    subprocess.run(["pip", "install", package], check=None)


def x_install_selected_providers__mutmut_8(selected: list[str] | None) -> None:
    """
    Install selected provider extras via pip after user choice in SetupWizard.
    Called from SetupWizardScreen step 2 when user clicks 'Install Selected'.
    Does nothing if selected is empty (vanilla only).
    """
    if not selected:
        return
    extras = ",".join(selected)
    package = f"hexawyn[{extras}]"
    subprocess.run(check=True)


def x_install_selected_providers__mutmut_9(selected: list[str] | None) -> None:
    """
    Install selected provider extras via pip after user choice in SetupWizard.
    Called from SetupWizardScreen step 2 when user clicks 'Install Selected'.
    Does nothing if selected is empty (vanilla only).
    """
    if not selected:
        return
    extras = ",".join(selected)
    package = f"hexawyn[{extras}]"
    subprocess.run(["pip", "install", package], )


def x_install_selected_providers__mutmut_10(selected: list[str] | None) -> None:
    """
    Install selected provider extras via pip after user choice in SetupWizard.
    Called from SetupWizardScreen step 2 when user clicks 'Install Selected'.
    Does nothing if selected is empty (vanilla only).
    """
    if not selected:
        return
    extras = ",".join(selected)
    package = f"hexawyn[{extras}]"
    subprocess.run(["XXpipXX", "install", package], check=True)


def x_install_selected_providers__mutmut_11(selected: list[str] | None) -> None:
    """
    Install selected provider extras via pip after user choice in SetupWizard.
    Called from SetupWizardScreen step 2 when user clicks 'Install Selected'.
    Does nothing if selected is empty (vanilla only).
    """
    if not selected:
        return
    extras = ",".join(selected)
    package = f"hexawyn[{extras}]"
    subprocess.run(["PIP", "install", package], check=True)


def x_install_selected_providers__mutmut_12(selected: list[str] | None) -> None:
    """
    Install selected provider extras via pip after user choice in SetupWizard.
    Called from SetupWizardScreen step 2 when user clicks 'Install Selected'.
    Does nothing if selected is empty (vanilla only).
    """
    if not selected:
        return
    extras = ",".join(selected)
    package = f"hexawyn[{extras}]"
    subprocess.run(["pip", "XXinstallXX", package], check=True)


def x_install_selected_providers__mutmut_13(selected: list[str] | None) -> None:
    """
    Install selected provider extras via pip after user choice in SetupWizard.
    Called from SetupWizardScreen step 2 when user clicks 'Install Selected'.
    Does nothing if selected is empty (vanilla only).
    """
    if not selected:
        return
    extras = ",".join(selected)
    package = f"hexawyn[{extras}]"
    subprocess.run(["pip", "INSTALL", package], check=True)


def x_install_selected_providers__mutmut_14(selected: list[str] | None) -> None:
    """
    Install selected provider extras via pip after user choice in SetupWizard.
    Called from SetupWizardScreen step 2 when user clicks 'Install Selected'.
    Does nothing if selected is empty (vanilla only).
    """
    if not selected:
        return
    extras = ",".join(selected)
    package = f"hexawyn[{extras}]"
    subprocess.run(["pip", "install", package], check=False)

mutants_x_install_selected_providers__mutmut['_mutmut_orig'] = x_install_selected_providers__mutmut_orig # type: ignore # mutmut generated
mutants_x_install_selected_providers__mutmut['x_install_selected_providers__mutmut_1'] = x_install_selected_providers__mutmut_1 # type: ignore # mutmut generated
mutants_x_install_selected_providers__mutmut['x_install_selected_providers__mutmut_2'] = x_install_selected_providers__mutmut_2 # type: ignore # mutmut generated
mutants_x_install_selected_providers__mutmut['x_install_selected_providers__mutmut_3'] = x_install_selected_providers__mutmut_3 # type: ignore # mutmut generated
mutants_x_install_selected_providers__mutmut['x_install_selected_providers__mutmut_4'] = x_install_selected_providers__mutmut_4 # type: ignore # mutmut generated
mutants_x_install_selected_providers__mutmut['x_install_selected_providers__mutmut_5'] = x_install_selected_providers__mutmut_5 # type: ignore # mutmut generated
mutants_x_install_selected_providers__mutmut['x_install_selected_providers__mutmut_6'] = x_install_selected_providers__mutmut_6 # type: ignore # mutmut generated
mutants_x_install_selected_providers__mutmut['x_install_selected_providers__mutmut_7'] = x_install_selected_providers__mutmut_7 # type: ignore # mutmut generated
mutants_x_install_selected_providers__mutmut['x_install_selected_providers__mutmut_8'] = x_install_selected_providers__mutmut_8 # type: ignore # mutmut generated
mutants_x_install_selected_providers__mutmut['x_install_selected_providers__mutmut_9'] = x_install_selected_providers__mutmut_9 # type: ignore # mutmut generated
mutants_x_install_selected_providers__mutmut['x_install_selected_providers__mutmut_10'] = x_install_selected_providers__mutmut_10 # type: ignore # mutmut generated
mutants_x_install_selected_providers__mutmut['x_install_selected_providers__mutmut_11'] = x_install_selected_providers__mutmut_11 # type: ignore # mutmut generated
mutants_x_install_selected_providers__mutmut['x_install_selected_providers__mutmut_12'] = x_install_selected_providers__mutmut_12 # type: ignore # mutmut generated
mutants_x_install_selected_providers__mutmut['x_install_selected_providers__mutmut_13'] = x_install_selected_providers__mutmut_13 # type: ignore # mutmut generated
mutants_x_install_selected_providers__mutmut['x_install_selected_providers__mutmut_14'] = x_install_selected_providers__mutmut_14 # type: ignore # mutmut generated
