def detect_installed_providers() -> dict[str, bool]:
    """
    Check which provider packages are installed by attempting imports.
    Used by AdapterFactory and /config providers command.
    Never raises — always returns a dict with boolean values.
    """
    providers: dict[str, bool] = {"vanilla": True}  # always available

    try:
        import boto3  # noqa: F401

        providers["aws"] = True
    except ImportError:
        providers["aws"] = False

    try:
        import azure.identity  # noqa: F401

        providers["azure"] = True
    except ImportError:
        providers["azure"] = False

    try:
        import google.cloud.container  # noqa: F401

        providers["gcp"] = True
    except ImportError:
        providers["gcp"] = False

    try:
        import openshift  # noqa: F401

        providers["openshift"] = True
    except ImportError:
        providers["openshift"] = False

    try:
        import datadog_api_client  # noqa: F401

        providers["datadog"] = True
    except ImportError:
        providers["datadog"] = False

    return providers
