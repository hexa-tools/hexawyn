import click
from dotenv import load_dotenv

load_dotenv()


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@click.group(invoke_without_command=True)
def app() -> None:
    """hexawyn — AI-powered Kubernetes diagnostic agent."""
    if not click.get_current_context().invoked_subcommand:
        from hexawyn.cli.presentation.feedback import header

        header()
        click.echo(app.get_help(click.get_current_context()))


def _register_start(start_group: click.Group) -> None:
    """Register the `start` command (the only TUI launcher) on the CLI group."""

    @start_group.command()
    @click.option("--demo", is_flag=True, help="Start in demo mode (no real cluster needed)")
    @click.option(
        "--scenario",
        default="aws_eks",
        type=click.Choice(["aws_eks", "azure_aks", "gcp_gke", "openshift", "datadog"]),
        help="Demo scenario to use",
    )
    @click.option("--expert", is_flag=True, help="Expert mode: raw JSON, no suggestion chips")
    @click.option("--no-cloud", is_flag=True, help="Start in local/BYOK mode (no Cloud auth)")
    def start(demo: bool, scenario: str, expert: bool, no_cloud: bool) -> None:
        """Start the hexawyn TUI (Cloud auth, or local/BYOK with --no-cloud)."""
        _welcome()

        import os

        if no_cloud:
            os.environ["HEXAWYN_RUNTIME_MODE"] = "embedded"

        if demo:
            os.environ["HEXAWYN_DEMO_MODE"] = "true"
            os.environ["HEXAWYN_DEMO_SCENARIO"] = scenario
        elif not no_cloud and not _cloud_auth_ready():
            os.environ["HEXAWYN_RUNTIME_MODE"] = "embedded"

        from hexawyn.cli.app import HexawynApp

        HexawynApp(expert_mode=expert).run()
mutants_x__cloud_auth_ready__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__cloud_auth_ready__mutmut)
def _cloud_auth_ready() -> bool:
    """Validate an existing/entered cloud token via the Control Plane.

    Returns True when a valid cloud token is active (and stored), otherwise the
    caller falls back to local/BYOK (embedded) mode.
    """
    import httpx

    from hexawyn.application.service.login_service import LoginService
    from hexawyn.domain.models.auth import LoginOutcome
    from hexawyn.infrastructure.adapters.secondary.auth.cloud_auth_adapter import CloudAuthAdapter
    from hexawyn.infrastructure.adapters.secondary.auth.config_token_store import ConfigTokenStore
    from hexawyn.infrastructure.adapters.secondary.auth.token_validator import HttpTokenValidator
    from hexawyn.infrastructure.config.config_manager import get_runtime_endpoint

    adapter = CloudAuthAdapter(
        validator=HttpTokenValidator(httpx.Client(), get_runtime_endpoint() or ""),
        store=ConfigTokenStore(),
    )
    service = LoginService(
        auth=adapter,
        prompt_token=_prompt_token,
        emit=click.echo,
        app_start=lambda: None,
    )
    outcome = service.authenticate()
    return outcome in (LoginOutcome.AUTHENTICATED, LoginOutcome.STARTED_WITH_EXISTING)


def x__cloud_auth_ready__mutmut_orig() -> bool:
    """Validate an existing/entered cloud token via the Control Plane.

    Returns True when a valid cloud token is active (and stored), otherwise the
    caller falls back to local/BYOK (embedded) mode.
    """
    import httpx

    from hexawyn.application.service.login_service import LoginService
    from hexawyn.domain.models.auth import LoginOutcome
    from hexawyn.infrastructure.adapters.secondary.auth.cloud_auth_adapter import CloudAuthAdapter
    from hexawyn.infrastructure.adapters.secondary.auth.config_token_store import ConfigTokenStore
    from hexawyn.infrastructure.adapters.secondary.auth.token_validator import HttpTokenValidator
    from hexawyn.infrastructure.config.config_manager import get_runtime_endpoint

    adapter = CloudAuthAdapter(
        validator=HttpTokenValidator(httpx.Client(), get_runtime_endpoint() or ""),
        store=ConfigTokenStore(),
    )
    service = LoginService(
        auth=adapter,
        prompt_token=_prompt_token,
        emit=click.echo,
        app_start=lambda: None,
    )
    outcome = service.authenticate()
    return outcome in (LoginOutcome.AUTHENTICATED, LoginOutcome.STARTED_WITH_EXISTING)


def x__cloud_auth_ready__mutmut_1() -> bool:
    """Validate an existing/entered cloud token via the Control Plane.

    Returns True when a valid cloud token is active (and stored), otherwise the
    caller falls back to local/BYOK (embedded) mode.
    """
    import httpx

    from hexawyn.application.service.login_service import LoginService
    from hexawyn.domain.models.auth import LoginOutcome
    from hexawyn.infrastructure.adapters.secondary.auth.cloud_auth_adapter import CloudAuthAdapter
    from hexawyn.infrastructure.adapters.secondary.auth.config_token_store import ConfigTokenStore
    from hexawyn.infrastructure.adapters.secondary.auth.token_validator import HttpTokenValidator
    from hexawyn.infrastructure.config.config_manager import get_runtime_endpoint

    adapter = None
    service = LoginService(
        auth=adapter,
        prompt_token=_prompt_token,
        emit=click.echo,
        app_start=lambda: None,
    )
    outcome = service.authenticate()
    return outcome in (LoginOutcome.AUTHENTICATED, LoginOutcome.STARTED_WITH_EXISTING)


def x__cloud_auth_ready__mutmut_2() -> bool:
    """Validate an existing/entered cloud token via the Control Plane.

    Returns True when a valid cloud token is active (and stored), otherwise the
    caller falls back to local/BYOK (embedded) mode.
    """
    import httpx

    from hexawyn.application.service.login_service import LoginService
    from hexawyn.domain.models.auth import LoginOutcome
    from hexawyn.infrastructure.adapters.secondary.auth.cloud_auth_adapter import CloudAuthAdapter
    from hexawyn.infrastructure.adapters.secondary.auth.config_token_store import ConfigTokenStore
    from hexawyn.infrastructure.adapters.secondary.auth.token_validator import HttpTokenValidator
    from hexawyn.infrastructure.config.config_manager import get_runtime_endpoint

    adapter = CloudAuthAdapter(
        validator=None,
        store=ConfigTokenStore(),
    )
    service = LoginService(
        auth=adapter,
        prompt_token=_prompt_token,
        emit=click.echo,
        app_start=lambda: None,
    )
    outcome = service.authenticate()
    return outcome in (LoginOutcome.AUTHENTICATED, LoginOutcome.STARTED_WITH_EXISTING)


def x__cloud_auth_ready__mutmut_3() -> bool:
    """Validate an existing/entered cloud token via the Control Plane.

    Returns True when a valid cloud token is active (and stored), otherwise the
    caller falls back to local/BYOK (embedded) mode.
    """
    import httpx

    from hexawyn.application.service.login_service import LoginService
    from hexawyn.domain.models.auth import LoginOutcome
    from hexawyn.infrastructure.adapters.secondary.auth.cloud_auth_adapter import CloudAuthAdapter
    from hexawyn.infrastructure.adapters.secondary.auth.config_token_store import ConfigTokenStore
    from hexawyn.infrastructure.adapters.secondary.auth.token_validator import HttpTokenValidator
    from hexawyn.infrastructure.config.config_manager import get_runtime_endpoint

    adapter = CloudAuthAdapter(
        validator=HttpTokenValidator(httpx.Client(), get_runtime_endpoint() or ""),
        store=None,
    )
    service = LoginService(
        auth=adapter,
        prompt_token=_prompt_token,
        emit=click.echo,
        app_start=lambda: None,
    )
    outcome = service.authenticate()
    return outcome in (LoginOutcome.AUTHENTICATED, LoginOutcome.STARTED_WITH_EXISTING)


def x__cloud_auth_ready__mutmut_4() -> bool:
    """Validate an existing/entered cloud token via the Control Plane.

    Returns True when a valid cloud token is active (and stored), otherwise the
    caller falls back to local/BYOK (embedded) mode.
    """
    import httpx

    from hexawyn.application.service.login_service import LoginService
    from hexawyn.domain.models.auth import LoginOutcome
    from hexawyn.infrastructure.adapters.secondary.auth.cloud_auth_adapter import CloudAuthAdapter
    from hexawyn.infrastructure.adapters.secondary.auth.config_token_store import ConfigTokenStore
    from hexawyn.infrastructure.adapters.secondary.auth.token_validator import HttpTokenValidator
    from hexawyn.infrastructure.config.config_manager import get_runtime_endpoint

    adapter = CloudAuthAdapter(
        store=ConfigTokenStore(),
    )
    service = LoginService(
        auth=adapter,
        prompt_token=_prompt_token,
        emit=click.echo,
        app_start=lambda: None,
    )
    outcome = service.authenticate()
    return outcome in (LoginOutcome.AUTHENTICATED, LoginOutcome.STARTED_WITH_EXISTING)


def x__cloud_auth_ready__mutmut_5() -> bool:
    """Validate an existing/entered cloud token via the Control Plane.

    Returns True when a valid cloud token is active (and stored), otherwise the
    caller falls back to local/BYOK (embedded) mode.
    """
    import httpx

    from hexawyn.application.service.login_service import LoginService
    from hexawyn.domain.models.auth import LoginOutcome
    from hexawyn.infrastructure.adapters.secondary.auth.cloud_auth_adapter import CloudAuthAdapter
    from hexawyn.infrastructure.adapters.secondary.auth.config_token_store import ConfigTokenStore
    from hexawyn.infrastructure.adapters.secondary.auth.token_validator import HttpTokenValidator
    from hexawyn.infrastructure.config.config_manager import get_runtime_endpoint

    adapter = CloudAuthAdapter(
        validator=HttpTokenValidator(httpx.Client(), get_runtime_endpoint() or ""),
        )
    service = LoginService(
        auth=adapter,
        prompt_token=_prompt_token,
        emit=click.echo,
        app_start=lambda: None,
    )
    outcome = service.authenticate()
    return outcome in (LoginOutcome.AUTHENTICATED, LoginOutcome.STARTED_WITH_EXISTING)


def x__cloud_auth_ready__mutmut_6() -> bool:
    """Validate an existing/entered cloud token via the Control Plane.

    Returns True when a valid cloud token is active (and stored), otherwise the
    caller falls back to local/BYOK (embedded) mode.
    """
    import httpx

    from hexawyn.application.service.login_service import LoginService
    from hexawyn.domain.models.auth import LoginOutcome
    from hexawyn.infrastructure.adapters.secondary.auth.cloud_auth_adapter import CloudAuthAdapter
    from hexawyn.infrastructure.adapters.secondary.auth.config_token_store import ConfigTokenStore
    from hexawyn.infrastructure.adapters.secondary.auth.token_validator import HttpTokenValidator
    from hexawyn.infrastructure.config.config_manager import get_runtime_endpoint

    adapter = CloudAuthAdapter(
        validator=HttpTokenValidator(None, get_runtime_endpoint() or ""),
        store=ConfigTokenStore(),
    )
    service = LoginService(
        auth=adapter,
        prompt_token=_prompt_token,
        emit=click.echo,
        app_start=lambda: None,
    )
    outcome = service.authenticate()
    return outcome in (LoginOutcome.AUTHENTICATED, LoginOutcome.STARTED_WITH_EXISTING)


def x__cloud_auth_ready__mutmut_7() -> bool:
    """Validate an existing/entered cloud token via the Control Plane.

    Returns True when a valid cloud token is active (and stored), otherwise the
    caller falls back to local/BYOK (embedded) mode.
    """
    import httpx

    from hexawyn.application.service.login_service import LoginService
    from hexawyn.domain.models.auth import LoginOutcome
    from hexawyn.infrastructure.adapters.secondary.auth.cloud_auth_adapter import CloudAuthAdapter
    from hexawyn.infrastructure.adapters.secondary.auth.config_token_store import ConfigTokenStore
    from hexawyn.infrastructure.adapters.secondary.auth.token_validator import HttpTokenValidator
    from hexawyn.infrastructure.config.config_manager import get_runtime_endpoint

    adapter = CloudAuthAdapter(
        validator=HttpTokenValidator(httpx.Client(), None),
        store=ConfigTokenStore(),
    )
    service = LoginService(
        auth=adapter,
        prompt_token=_prompt_token,
        emit=click.echo,
        app_start=lambda: None,
    )
    outcome = service.authenticate()
    return outcome in (LoginOutcome.AUTHENTICATED, LoginOutcome.STARTED_WITH_EXISTING)


def x__cloud_auth_ready__mutmut_8() -> bool:
    """Validate an existing/entered cloud token via the Control Plane.

    Returns True when a valid cloud token is active (and stored), otherwise the
    caller falls back to local/BYOK (embedded) mode.
    """
    import httpx

    from hexawyn.application.service.login_service import LoginService
    from hexawyn.domain.models.auth import LoginOutcome
    from hexawyn.infrastructure.adapters.secondary.auth.cloud_auth_adapter import CloudAuthAdapter
    from hexawyn.infrastructure.adapters.secondary.auth.config_token_store import ConfigTokenStore
    from hexawyn.infrastructure.adapters.secondary.auth.token_validator import HttpTokenValidator
    from hexawyn.infrastructure.config.config_manager import get_runtime_endpoint

    adapter = CloudAuthAdapter(
        validator=HttpTokenValidator(get_runtime_endpoint() or ""),
        store=ConfigTokenStore(),
    )
    service = LoginService(
        auth=adapter,
        prompt_token=_prompt_token,
        emit=click.echo,
        app_start=lambda: None,
    )
    outcome = service.authenticate()
    return outcome in (LoginOutcome.AUTHENTICATED, LoginOutcome.STARTED_WITH_EXISTING)


def x__cloud_auth_ready__mutmut_9() -> bool:
    """Validate an existing/entered cloud token via the Control Plane.

    Returns True when a valid cloud token is active (and stored), otherwise the
    caller falls back to local/BYOK (embedded) mode.
    """
    import httpx

    from hexawyn.application.service.login_service import LoginService
    from hexawyn.domain.models.auth import LoginOutcome
    from hexawyn.infrastructure.adapters.secondary.auth.cloud_auth_adapter import CloudAuthAdapter
    from hexawyn.infrastructure.adapters.secondary.auth.config_token_store import ConfigTokenStore
    from hexawyn.infrastructure.adapters.secondary.auth.token_validator import HttpTokenValidator
    from hexawyn.infrastructure.config.config_manager import get_runtime_endpoint

    adapter = CloudAuthAdapter(
        validator=HttpTokenValidator(httpx.Client(), ),
        store=ConfigTokenStore(),
    )
    service = LoginService(
        auth=adapter,
        prompt_token=_prompt_token,
        emit=click.echo,
        app_start=lambda: None,
    )
    outcome = service.authenticate()
    return outcome in (LoginOutcome.AUTHENTICATED, LoginOutcome.STARTED_WITH_EXISTING)


def x__cloud_auth_ready__mutmut_10() -> bool:
    """Validate an existing/entered cloud token via the Control Plane.

    Returns True when a valid cloud token is active (and stored), otherwise the
    caller falls back to local/BYOK (embedded) mode.
    """
    import httpx

    from hexawyn.application.service.login_service import LoginService
    from hexawyn.domain.models.auth import LoginOutcome
    from hexawyn.infrastructure.adapters.secondary.auth.cloud_auth_adapter import CloudAuthAdapter
    from hexawyn.infrastructure.adapters.secondary.auth.config_token_store import ConfigTokenStore
    from hexawyn.infrastructure.adapters.secondary.auth.token_validator import HttpTokenValidator
    from hexawyn.infrastructure.config.config_manager import get_runtime_endpoint

    adapter = CloudAuthAdapter(
        validator=HttpTokenValidator(httpx.Client(), get_runtime_endpoint() and ""),
        store=ConfigTokenStore(),
    )
    service = LoginService(
        auth=adapter,
        prompt_token=_prompt_token,
        emit=click.echo,
        app_start=lambda: None,
    )
    outcome = service.authenticate()
    return outcome in (LoginOutcome.AUTHENTICATED, LoginOutcome.STARTED_WITH_EXISTING)


def x__cloud_auth_ready__mutmut_11() -> bool:
    """Validate an existing/entered cloud token via the Control Plane.

    Returns True when a valid cloud token is active (and stored), otherwise the
    caller falls back to local/BYOK (embedded) mode.
    """
    import httpx

    from hexawyn.application.service.login_service import LoginService
    from hexawyn.domain.models.auth import LoginOutcome
    from hexawyn.infrastructure.adapters.secondary.auth.cloud_auth_adapter import CloudAuthAdapter
    from hexawyn.infrastructure.adapters.secondary.auth.config_token_store import ConfigTokenStore
    from hexawyn.infrastructure.adapters.secondary.auth.token_validator import HttpTokenValidator
    from hexawyn.infrastructure.config.config_manager import get_runtime_endpoint

    adapter = CloudAuthAdapter(
        validator=HttpTokenValidator(httpx.Client(), get_runtime_endpoint() or "XXXX"),
        store=ConfigTokenStore(),
    )
    service = LoginService(
        auth=adapter,
        prompt_token=_prompt_token,
        emit=click.echo,
        app_start=lambda: None,
    )
    outcome = service.authenticate()
    return outcome in (LoginOutcome.AUTHENTICATED, LoginOutcome.STARTED_WITH_EXISTING)


def x__cloud_auth_ready__mutmut_12() -> bool:
    """Validate an existing/entered cloud token via the Control Plane.

    Returns True when a valid cloud token is active (and stored), otherwise the
    caller falls back to local/BYOK (embedded) mode.
    """
    import httpx

    from hexawyn.application.service.login_service import LoginService
    from hexawyn.domain.models.auth import LoginOutcome
    from hexawyn.infrastructure.adapters.secondary.auth.cloud_auth_adapter import CloudAuthAdapter
    from hexawyn.infrastructure.adapters.secondary.auth.config_token_store import ConfigTokenStore
    from hexawyn.infrastructure.adapters.secondary.auth.token_validator import HttpTokenValidator
    from hexawyn.infrastructure.config.config_manager import get_runtime_endpoint

    adapter = CloudAuthAdapter(
        validator=HttpTokenValidator(httpx.Client(), get_runtime_endpoint() or ""),
        store=ConfigTokenStore(),
    )
    service = None
    outcome = service.authenticate()
    return outcome in (LoginOutcome.AUTHENTICATED, LoginOutcome.STARTED_WITH_EXISTING)


def x__cloud_auth_ready__mutmut_13() -> bool:
    """Validate an existing/entered cloud token via the Control Plane.

    Returns True when a valid cloud token is active (and stored), otherwise the
    caller falls back to local/BYOK (embedded) mode.
    """
    import httpx

    from hexawyn.application.service.login_service import LoginService
    from hexawyn.domain.models.auth import LoginOutcome
    from hexawyn.infrastructure.adapters.secondary.auth.cloud_auth_adapter import CloudAuthAdapter
    from hexawyn.infrastructure.adapters.secondary.auth.config_token_store import ConfigTokenStore
    from hexawyn.infrastructure.adapters.secondary.auth.token_validator import HttpTokenValidator
    from hexawyn.infrastructure.config.config_manager import get_runtime_endpoint

    adapter = CloudAuthAdapter(
        validator=HttpTokenValidator(httpx.Client(), get_runtime_endpoint() or ""),
        store=ConfigTokenStore(),
    )
    service = LoginService(
        auth=None,
        prompt_token=_prompt_token,
        emit=click.echo,
        app_start=lambda: None,
    )
    outcome = service.authenticate()
    return outcome in (LoginOutcome.AUTHENTICATED, LoginOutcome.STARTED_WITH_EXISTING)


def x__cloud_auth_ready__mutmut_14() -> bool:
    """Validate an existing/entered cloud token via the Control Plane.

    Returns True when a valid cloud token is active (and stored), otherwise the
    caller falls back to local/BYOK (embedded) mode.
    """
    import httpx

    from hexawyn.application.service.login_service import LoginService
    from hexawyn.domain.models.auth import LoginOutcome
    from hexawyn.infrastructure.adapters.secondary.auth.cloud_auth_adapter import CloudAuthAdapter
    from hexawyn.infrastructure.adapters.secondary.auth.config_token_store import ConfigTokenStore
    from hexawyn.infrastructure.adapters.secondary.auth.token_validator import HttpTokenValidator
    from hexawyn.infrastructure.config.config_manager import get_runtime_endpoint

    adapter = CloudAuthAdapter(
        validator=HttpTokenValidator(httpx.Client(), get_runtime_endpoint() or ""),
        store=ConfigTokenStore(),
    )
    service = LoginService(
        auth=adapter,
        prompt_token=None,
        emit=click.echo,
        app_start=lambda: None,
    )
    outcome = service.authenticate()
    return outcome in (LoginOutcome.AUTHENTICATED, LoginOutcome.STARTED_WITH_EXISTING)


def x__cloud_auth_ready__mutmut_15() -> bool:
    """Validate an existing/entered cloud token via the Control Plane.

    Returns True when a valid cloud token is active (and stored), otherwise the
    caller falls back to local/BYOK (embedded) mode.
    """
    import httpx

    from hexawyn.application.service.login_service import LoginService
    from hexawyn.domain.models.auth import LoginOutcome
    from hexawyn.infrastructure.adapters.secondary.auth.cloud_auth_adapter import CloudAuthAdapter
    from hexawyn.infrastructure.adapters.secondary.auth.config_token_store import ConfigTokenStore
    from hexawyn.infrastructure.adapters.secondary.auth.token_validator import HttpTokenValidator
    from hexawyn.infrastructure.config.config_manager import get_runtime_endpoint

    adapter = CloudAuthAdapter(
        validator=HttpTokenValidator(httpx.Client(), get_runtime_endpoint() or ""),
        store=ConfigTokenStore(),
    )
    service = LoginService(
        auth=adapter,
        prompt_token=_prompt_token,
        emit=None,
        app_start=lambda: None,
    )
    outcome = service.authenticate()
    return outcome in (LoginOutcome.AUTHENTICATED, LoginOutcome.STARTED_WITH_EXISTING)


def x__cloud_auth_ready__mutmut_16() -> bool:
    """Validate an existing/entered cloud token via the Control Plane.

    Returns True when a valid cloud token is active (and stored), otherwise the
    caller falls back to local/BYOK (embedded) mode.
    """
    import httpx

    from hexawyn.application.service.login_service import LoginService
    from hexawyn.domain.models.auth import LoginOutcome
    from hexawyn.infrastructure.adapters.secondary.auth.cloud_auth_adapter import CloudAuthAdapter
    from hexawyn.infrastructure.adapters.secondary.auth.config_token_store import ConfigTokenStore
    from hexawyn.infrastructure.adapters.secondary.auth.token_validator import HttpTokenValidator
    from hexawyn.infrastructure.config.config_manager import get_runtime_endpoint

    adapter = CloudAuthAdapter(
        validator=HttpTokenValidator(httpx.Client(), get_runtime_endpoint() or ""),
        store=ConfigTokenStore(),
    )
    service = LoginService(
        auth=adapter,
        prompt_token=_prompt_token,
        emit=click.echo,
        app_start=None,
    )
    outcome = service.authenticate()
    return outcome in (LoginOutcome.AUTHENTICATED, LoginOutcome.STARTED_WITH_EXISTING)


def x__cloud_auth_ready__mutmut_17() -> bool:
    """Validate an existing/entered cloud token via the Control Plane.

    Returns True when a valid cloud token is active (and stored), otherwise the
    caller falls back to local/BYOK (embedded) mode.
    """
    import httpx

    from hexawyn.application.service.login_service import LoginService
    from hexawyn.domain.models.auth import LoginOutcome
    from hexawyn.infrastructure.adapters.secondary.auth.cloud_auth_adapter import CloudAuthAdapter
    from hexawyn.infrastructure.adapters.secondary.auth.config_token_store import ConfigTokenStore
    from hexawyn.infrastructure.adapters.secondary.auth.token_validator import HttpTokenValidator
    from hexawyn.infrastructure.config.config_manager import get_runtime_endpoint

    adapter = CloudAuthAdapter(
        validator=HttpTokenValidator(httpx.Client(), get_runtime_endpoint() or ""),
        store=ConfigTokenStore(),
    )
    service = LoginService(
        prompt_token=_prompt_token,
        emit=click.echo,
        app_start=lambda: None,
    )
    outcome = service.authenticate()
    return outcome in (LoginOutcome.AUTHENTICATED, LoginOutcome.STARTED_WITH_EXISTING)


def x__cloud_auth_ready__mutmut_18() -> bool:
    """Validate an existing/entered cloud token via the Control Plane.

    Returns True when a valid cloud token is active (and stored), otherwise the
    caller falls back to local/BYOK (embedded) mode.
    """
    import httpx

    from hexawyn.application.service.login_service import LoginService
    from hexawyn.domain.models.auth import LoginOutcome
    from hexawyn.infrastructure.adapters.secondary.auth.cloud_auth_adapter import CloudAuthAdapter
    from hexawyn.infrastructure.adapters.secondary.auth.config_token_store import ConfigTokenStore
    from hexawyn.infrastructure.adapters.secondary.auth.token_validator import HttpTokenValidator
    from hexawyn.infrastructure.config.config_manager import get_runtime_endpoint

    adapter = CloudAuthAdapter(
        validator=HttpTokenValidator(httpx.Client(), get_runtime_endpoint() or ""),
        store=ConfigTokenStore(),
    )
    service = LoginService(
        auth=adapter,
        emit=click.echo,
        app_start=lambda: None,
    )
    outcome = service.authenticate()
    return outcome in (LoginOutcome.AUTHENTICATED, LoginOutcome.STARTED_WITH_EXISTING)


def x__cloud_auth_ready__mutmut_19() -> bool:
    """Validate an existing/entered cloud token via the Control Plane.

    Returns True when a valid cloud token is active (and stored), otherwise the
    caller falls back to local/BYOK (embedded) mode.
    """
    import httpx

    from hexawyn.application.service.login_service import LoginService
    from hexawyn.domain.models.auth import LoginOutcome
    from hexawyn.infrastructure.adapters.secondary.auth.cloud_auth_adapter import CloudAuthAdapter
    from hexawyn.infrastructure.adapters.secondary.auth.config_token_store import ConfigTokenStore
    from hexawyn.infrastructure.adapters.secondary.auth.token_validator import HttpTokenValidator
    from hexawyn.infrastructure.config.config_manager import get_runtime_endpoint

    adapter = CloudAuthAdapter(
        validator=HttpTokenValidator(httpx.Client(), get_runtime_endpoint() or ""),
        store=ConfigTokenStore(),
    )
    service = LoginService(
        auth=adapter,
        prompt_token=_prompt_token,
        app_start=lambda: None,
    )
    outcome = service.authenticate()
    return outcome in (LoginOutcome.AUTHENTICATED, LoginOutcome.STARTED_WITH_EXISTING)


def x__cloud_auth_ready__mutmut_20() -> bool:
    """Validate an existing/entered cloud token via the Control Plane.

    Returns True when a valid cloud token is active (and stored), otherwise the
    caller falls back to local/BYOK (embedded) mode.
    """
    import httpx

    from hexawyn.application.service.login_service import LoginService
    from hexawyn.domain.models.auth import LoginOutcome
    from hexawyn.infrastructure.adapters.secondary.auth.cloud_auth_adapter import CloudAuthAdapter
    from hexawyn.infrastructure.adapters.secondary.auth.config_token_store import ConfigTokenStore
    from hexawyn.infrastructure.adapters.secondary.auth.token_validator import HttpTokenValidator
    from hexawyn.infrastructure.config.config_manager import get_runtime_endpoint

    adapter = CloudAuthAdapter(
        validator=HttpTokenValidator(httpx.Client(), get_runtime_endpoint() or ""),
        store=ConfigTokenStore(),
    )
    service = LoginService(
        auth=adapter,
        prompt_token=_prompt_token,
        emit=click.echo,
        )
    outcome = service.authenticate()
    return outcome in (LoginOutcome.AUTHENTICATED, LoginOutcome.STARTED_WITH_EXISTING)


def x__cloud_auth_ready__mutmut_21() -> bool:
    """Validate an existing/entered cloud token via the Control Plane.

    Returns True when a valid cloud token is active (and stored), otherwise the
    caller falls back to local/BYOK (embedded) mode.
    """
    import httpx

    from hexawyn.application.service.login_service import LoginService
    from hexawyn.domain.models.auth import LoginOutcome
    from hexawyn.infrastructure.adapters.secondary.auth.cloud_auth_adapter import CloudAuthAdapter
    from hexawyn.infrastructure.adapters.secondary.auth.config_token_store import ConfigTokenStore
    from hexawyn.infrastructure.adapters.secondary.auth.token_validator import HttpTokenValidator
    from hexawyn.infrastructure.config.config_manager import get_runtime_endpoint

    adapter = CloudAuthAdapter(
        validator=HttpTokenValidator(httpx.Client(), get_runtime_endpoint() or ""),
        store=ConfigTokenStore(),
    )
    service = LoginService(
        auth=adapter,
        prompt_token=_prompt_token,
        emit=click.echo,
        app_start=lambda: 0,
    )
    outcome = service.authenticate()
    return outcome in (LoginOutcome.AUTHENTICATED, LoginOutcome.STARTED_WITH_EXISTING)


def x__cloud_auth_ready__mutmut_22() -> bool:
    """Validate an existing/entered cloud token via the Control Plane.

    Returns True when a valid cloud token is active (and stored), otherwise the
    caller falls back to local/BYOK (embedded) mode.
    """
    import httpx

    from hexawyn.application.service.login_service import LoginService
    from hexawyn.domain.models.auth import LoginOutcome
    from hexawyn.infrastructure.adapters.secondary.auth.cloud_auth_adapter import CloudAuthAdapter
    from hexawyn.infrastructure.adapters.secondary.auth.config_token_store import ConfigTokenStore
    from hexawyn.infrastructure.adapters.secondary.auth.token_validator import HttpTokenValidator
    from hexawyn.infrastructure.config.config_manager import get_runtime_endpoint

    adapter = CloudAuthAdapter(
        validator=HttpTokenValidator(httpx.Client(), get_runtime_endpoint() or ""),
        store=ConfigTokenStore(),
    )
    service = LoginService(
        auth=adapter,
        prompt_token=_prompt_token,
        emit=click.echo,
        app_start=lambda: None,
    )
    outcome = None
    return outcome in (LoginOutcome.AUTHENTICATED, LoginOutcome.STARTED_WITH_EXISTING)


def x__cloud_auth_ready__mutmut_23() -> bool:
    """Validate an existing/entered cloud token via the Control Plane.

    Returns True when a valid cloud token is active (and stored), otherwise the
    caller falls back to local/BYOK (embedded) mode.
    """
    import httpx

    from hexawyn.application.service.login_service import LoginService
    from hexawyn.domain.models.auth import LoginOutcome
    from hexawyn.infrastructure.adapters.secondary.auth.cloud_auth_adapter import CloudAuthAdapter
    from hexawyn.infrastructure.adapters.secondary.auth.config_token_store import ConfigTokenStore
    from hexawyn.infrastructure.adapters.secondary.auth.token_validator import HttpTokenValidator
    from hexawyn.infrastructure.config.config_manager import get_runtime_endpoint

    adapter = CloudAuthAdapter(
        validator=HttpTokenValidator(httpx.Client(), get_runtime_endpoint() or ""),
        store=ConfigTokenStore(),
    )
    service = LoginService(
        auth=adapter,
        prompt_token=_prompt_token,
        emit=click.echo,
        app_start=lambda: None,
    )
    outcome = service.authenticate()
    return outcome not in (LoginOutcome.AUTHENTICATED, LoginOutcome.STARTED_WITH_EXISTING)

mutants_x__cloud_auth_ready__mutmut['_mutmut_orig'] = x__cloud_auth_ready__mutmut_orig # type: ignore # mutmut generated
mutants_x__cloud_auth_ready__mutmut['x__cloud_auth_ready__mutmut_1'] = x__cloud_auth_ready__mutmut_1 # type: ignore # mutmut generated
mutants_x__cloud_auth_ready__mutmut['x__cloud_auth_ready__mutmut_2'] = x__cloud_auth_ready__mutmut_2 # type: ignore # mutmut generated
mutants_x__cloud_auth_ready__mutmut['x__cloud_auth_ready__mutmut_3'] = x__cloud_auth_ready__mutmut_3 # type: ignore # mutmut generated
mutants_x__cloud_auth_ready__mutmut['x__cloud_auth_ready__mutmut_4'] = x__cloud_auth_ready__mutmut_4 # type: ignore # mutmut generated
mutants_x__cloud_auth_ready__mutmut['x__cloud_auth_ready__mutmut_5'] = x__cloud_auth_ready__mutmut_5 # type: ignore # mutmut generated
mutants_x__cloud_auth_ready__mutmut['x__cloud_auth_ready__mutmut_6'] = x__cloud_auth_ready__mutmut_6 # type: ignore # mutmut generated
mutants_x__cloud_auth_ready__mutmut['x__cloud_auth_ready__mutmut_7'] = x__cloud_auth_ready__mutmut_7 # type: ignore # mutmut generated
mutants_x__cloud_auth_ready__mutmut['x__cloud_auth_ready__mutmut_8'] = x__cloud_auth_ready__mutmut_8 # type: ignore # mutmut generated
mutants_x__cloud_auth_ready__mutmut['x__cloud_auth_ready__mutmut_9'] = x__cloud_auth_ready__mutmut_9 # type: ignore # mutmut generated
mutants_x__cloud_auth_ready__mutmut['x__cloud_auth_ready__mutmut_10'] = x__cloud_auth_ready__mutmut_10 # type: ignore # mutmut generated
mutants_x__cloud_auth_ready__mutmut['x__cloud_auth_ready__mutmut_11'] = x__cloud_auth_ready__mutmut_11 # type: ignore # mutmut generated
mutants_x__cloud_auth_ready__mutmut['x__cloud_auth_ready__mutmut_12'] = x__cloud_auth_ready__mutmut_12 # type: ignore # mutmut generated
mutants_x__cloud_auth_ready__mutmut['x__cloud_auth_ready__mutmut_13'] = x__cloud_auth_ready__mutmut_13 # type: ignore # mutmut generated
mutants_x__cloud_auth_ready__mutmut['x__cloud_auth_ready__mutmut_14'] = x__cloud_auth_ready__mutmut_14 # type: ignore # mutmut generated
mutants_x__cloud_auth_ready__mutmut['x__cloud_auth_ready__mutmut_15'] = x__cloud_auth_ready__mutmut_15 # type: ignore # mutmut generated
mutants_x__cloud_auth_ready__mutmut['x__cloud_auth_ready__mutmut_16'] = x__cloud_auth_ready__mutmut_16 # type: ignore # mutmut generated
mutants_x__cloud_auth_ready__mutmut['x__cloud_auth_ready__mutmut_17'] = x__cloud_auth_ready__mutmut_17 # type: ignore # mutmut generated
mutants_x__cloud_auth_ready__mutmut['x__cloud_auth_ready__mutmut_18'] = x__cloud_auth_ready__mutmut_18 # type: ignore # mutmut generated
mutants_x__cloud_auth_ready__mutmut['x__cloud_auth_ready__mutmut_19'] = x__cloud_auth_ready__mutmut_19 # type: ignore # mutmut generated
mutants_x__cloud_auth_ready__mutmut['x__cloud_auth_ready__mutmut_20'] = x__cloud_auth_ready__mutmut_20 # type: ignore # mutmut generated
mutants_x__cloud_auth_ready__mutmut['x__cloud_auth_ready__mutmut_21'] = x__cloud_auth_ready__mutmut_21 # type: ignore # mutmut generated
mutants_x__cloud_auth_ready__mutmut['x__cloud_auth_ready__mutmut_22'] = x__cloud_auth_ready__mutmut_22 # type: ignore # mutmut generated
mutants_x__cloud_auth_ready__mutmut['x__cloud_auth_ready__mutmut_23'] = x__cloud_auth_ready__mutmut_23 # type: ignore # mutmut generated
mutants_x__prompt_token__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__prompt_token__mutmut)
def _prompt_token() -> str | None:
    """Prompt for the Hexawyn Cloud token using hidden input."""
    click.echo("  ✨ A Cloud token unlocks AI investigations against your cluster.")
    click.echo("     Press Ctrl+C to continue in local/BYOK mode (no cloud).")
    click.echo("")
    try:
        value = click.prompt("  Hexawyn Cloud token", hide_input=True, show_default=False)
        return value if isinstance(value, str) else None
    except (click.Abort, KeyboardInterrupt):
        return None


def x__prompt_token__mutmut_orig() -> str | None:
    """Prompt for the Hexawyn Cloud token using hidden input."""
    click.echo("  ✨ A Cloud token unlocks AI investigations against your cluster.")
    click.echo("     Press Ctrl+C to continue in local/BYOK mode (no cloud).")
    click.echo("")
    try:
        value = click.prompt("  Hexawyn Cloud token", hide_input=True, show_default=False)
        return value if isinstance(value, str) else None
    except (click.Abort, KeyboardInterrupt):
        return None


def x__prompt_token__mutmut_1() -> str | None:
    """Prompt for the Hexawyn Cloud token using hidden input."""
    click.echo(None)
    click.echo("     Press Ctrl+C to continue in local/BYOK mode (no cloud).")
    click.echo("")
    try:
        value = click.prompt("  Hexawyn Cloud token", hide_input=True, show_default=False)
        return value if isinstance(value, str) else None
    except (click.Abort, KeyboardInterrupt):
        return None


def x__prompt_token__mutmut_2() -> str | None:
    """Prompt for the Hexawyn Cloud token using hidden input."""
    click.echo("XX  ✨ A Cloud token unlocks AI investigations against your cluster.XX")
    click.echo("     Press Ctrl+C to continue in local/BYOK mode (no cloud).")
    click.echo("")
    try:
        value = click.prompt("  Hexawyn Cloud token", hide_input=True, show_default=False)
        return value if isinstance(value, str) else None
    except (click.Abort, KeyboardInterrupt):
        return None


def x__prompt_token__mutmut_3() -> str | None:
    """Prompt for the Hexawyn Cloud token using hidden input."""
    click.echo("  ✨ a cloud token unlocks ai investigations against your cluster.")
    click.echo("     Press Ctrl+C to continue in local/BYOK mode (no cloud).")
    click.echo("")
    try:
        value = click.prompt("  Hexawyn Cloud token", hide_input=True, show_default=False)
        return value if isinstance(value, str) else None
    except (click.Abort, KeyboardInterrupt):
        return None


def x__prompt_token__mutmut_4() -> str | None:
    """Prompt for the Hexawyn Cloud token using hidden input."""
    click.echo("  ✨ A CLOUD TOKEN UNLOCKS AI INVESTIGATIONS AGAINST YOUR CLUSTER.")
    click.echo("     Press Ctrl+C to continue in local/BYOK mode (no cloud).")
    click.echo("")
    try:
        value = click.prompt("  Hexawyn Cloud token", hide_input=True, show_default=False)
        return value if isinstance(value, str) else None
    except (click.Abort, KeyboardInterrupt):
        return None


def x__prompt_token__mutmut_5() -> str | None:
    """Prompt for the Hexawyn Cloud token using hidden input."""
    click.echo("  ✨ A Cloud token unlocks AI investigations against your cluster.")
    click.echo(None)
    click.echo("")
    try:
        value = click.prompt("  Hexawyn Cloud token", hide_input=True, show_default=False)
        return value if isinstance(value, str) else None
    except (click.Abort, KeyboardInterrupt):
        return None


def x__prompt_token__mutmut_6() -> str | None:
    """Prompt for the Hexawyn Cloud token using hidden input."""
    click.echo("  ✨ A Cloud token unlocks AI investigations against your cluster.")
    click.echo("XX     Press Ctrl+C to continue in local/BYOK mode (no cloud).XX")
    click.echo("")
    try:
        value = click.prompt("  Hexawyn Cloud token", hide_input=True, show_default=False)
        return value if isinstance(value, str) else None
    except (click.Abort, KeyboardInterrupt):
        return None


def x__prompt_token__mutmut_7() -> str | None:
    """Prompt for the Hexawyn Cloud token using hidden input."""
    click.echo("  ✨ A Cloud token unlocks AI investigations against your cluster.")
    click.echo("     press ctrl+c to continue in local/byok mode (no cloud).")
    click.echo("")
    try:
        value = click.prompt("  Hexawyn Cloud token", hide_input=True, show_default=False)
        return value if isinstance(value, str) else None
    except (click.Abort, KeyboardInterrupt):
        return None


def x__prompt_token__mutmut_8() -> str | None:
    """Prompt for the Hexawyn Cloud token using hidden input."""
    click.echo("  ✨ A Cloud token unlocks AI investigations against your cluster.")
    click.echo("     PRESS CTRL+C TO CONTINUE IN LOCAL/BYOK MODE (NO CLOUD).")
    click.echo("")
    try:
        value = click.prompt("  Hexawyn Cloud token", hide_input=True, show_default=False)
        return value if isinstance(value, str) else None
    except (click.Abort, KeyboardInterrupt):
        return None


def x__prompt_token__mutmut_9() -> str | None:
    """Prompt for the Hexawyn Cloud token using hidden input."""
    click.echo("  ✨ A Cloud token unlocks AI investigations against your cluster.")
    click.echo("     Press Ctrl+C to continue in local/BYOK mode (no cloud).")
    click.echo(None)
    try:
        value = click.prompt("  Hexawyn Cloud token", hide_input=True, show_default=False)
        return value if isinstance(value, str) else None
    except (click.Abort, KeyboardInterrupt):
        return None


def x__prompt_token__mutmut_10() -> str | None:
    """Prompt for the Hexawyn Cloud token using hidden input."""
    click.echo("  ✨ A Cloud token unlocks AI investigations against your cluster.")
    click.echo("     Press Ctrl+C to continue in local/BYOK mode (no cloud).")
    click.echo("XXXX")
    try:
        value = click.prompt("  Hexawyn Cloud token", hide_input=True, show_default=False)
        return value if isinstance(value, str) else None
    except (click.Abort, KeyboardInterrupt):
        return None


def x__prompt_token__mutmut_11() -> str | None:
    """Prompt for the Hexawyn Cloud token using hidden input."""
    click.echo("  ✨ A Cloud token unlocks AI investigations against your cluster.")
    click.echo("     Press Ctrl+C to continue in local/BYOK mode (no cloud).")
    click.echo("")
    try:
        value = None
        return value if isinstance(value, str) else None
    except (click.Abort, KeyboardInterrupt):
        return None


def x__prompt_token__mutmut_12() -> str | None:
    """Prompt for the Hexawyn Cloud token using hidden input."""
    click.echo("  ✨ A Cloud token unlocks AI investigations against your cluster.")
    click.echo("     Press Ctrl+C to continue in local/BYOK mode (no cloud).")
    click.echo("")
    try:
        value = click.prompt(None, hide_input=True, show_default=False)
        return value if isinstance(value, str) else None
    except (click.Abort, KeyboardInterrupt):
        return None


def x__prompt_token__mutmut_13() -> str | None:
    """Prompt for the Hexawyn Cloud token using hidden input."""
    click.echo("  ✨ A Cloud token unlocks AI investigations against your cluster.")
    click.echo("     Press Ctrl+C to continue in local/BYOK mode (no cloud).")
    click.echo("")
    try:
        value = click.prompt("  Hexawyn Cloud token", hide_input=None, show_default=False)
        return value if isinstance(value, str) else None
    except (click.Abort, KeyboardInterrupt):
        return None


def x__prompt_token__mutmut_14() -> str | None:
    """Prompt for the Hexawyn Cloud token using hidden input."""
    click.echo("  ✨ A Cloud token unlocks AI investigations against your cluster.")
    click.echo("     Press Ctrl+C to continue in local/BYOK mode (no cloud).")
    click.echo("")
    try:
        value = click.prompt("  Hexawyn Cloud token", hide_input=True, show_default=None)
        return value if isinstance(value, str) else None
    except (click.Abort, KeyboardInterrupt):
        return None


def x__prompt_token__mutmut_15() -> str | None:
    """Prompt for the Hexawyn Cloud token using hidden input."""
    click.echo("  ✨ A Cloud token unlocks AI investigations against your cluster.")
    click.echo("     Press Ctrl+C to continue in local/BYOK mode (no cloud).")
    click.echo("")
    try:
        value = click.prompt(hide_input=True, show_default=False)
        return value if isinstance(value, str) else None
    except (click.Abort, KeyboardInterrupt):
        return None


def x__prompt_token__mutmut_16() -> str | None:
    """Prompt for the Hexawyn Cloud token using hidden input."""
    click.echo("  ✨ A Cloud token unlocks AI investigations against your cluster.")
    click.echo("     Press Ctrl+C to continue in local/BYOK mode (no cloud).")
    click.echo("")
    try:
        value = click.prompt("  Hexawyn Cloud token", show_default=False)
        return value if isinstance(value, str) else None
    except (click.Abort, KeyboardInterrupt):
        return None


def x__prompt_token__mutmut_17() -> str | None:
    """Prompt for the Hexawyn Cloud token using hidden input."""
    click.echo("  ✨ A Cloud token unlocks AI investigations against your cluster.")
    click.echo("     Press Ctrl+C to continue in local/BYOK mode (no cloud).")
    click.echo("")
    try:
        value = click.prompt("  Hexawyn Cloud token", hide_input=True, )
        return value if isinstance(value, str) else None
    except (click.Abort, KeyboardInterrupt):
        return None


def x__prompt_token__mutmut_18() -> str | None:
    """Prompt for the Hexawyn Cloud token using hidden input."""
    click.echo("  ✨ A Cloud token unlocks AI investigations against your cluster.")
    click.echo("     Press Ctrl+C to continue in local/BYOK mode (no cloud).")
    click.echo("")
    try:
        value = click.prompt("XX  Hexawyn Cloud tokenXX", hide_input=True, show_default=False)
        return value if isinstance(value, str) else None
    except (click.Abort, KeyboardInterrupt):
        return None


def x__prompt_token__mutmut_19() -> str | None:
    """Prompt for the Hexawyn Cloud token using hidden input."""
    click.echo("  ✨ A Cloud token unlocks AI investigations against your cluster.")
    click.echo("     Press Ctrl+C to continue in local/BYOK mode (no cloud).")
    click.echo("")
    try:
        value = click.prompt("  hexawyn cloud token", hide_input=True, show_default=False)
        return value if isinstance(value, str) else None
    except (click.Abort, KeyboardInterrupt):
        return None


def x__prompt_token__mutmut_20() -> str | None:
    """Prompt for the Hexawyn Cloud token using hidden input."""
    click.echo("  ✨ A Cloud token unlocks AI investigations against your cluster.")
    click.echo("     Press Ctrl+C to continue in local/BYOK mode (no cloud).")
    click.echo("")
    try:
        value = click.prompt("  HEXAWYN CLOUD TOKEN", hide_input=True, show_default=False)
        return value if isinstance(value, str) else None
    except (click.Abort, KeyboardInterrupt):
        return None


def x__prompt_token__mutmut_21() -> str | None:
    """Prompt for the Hexawyn Cloud token using hidden input."""
    click.echo("  ✨ A Cloud token unlocks AI investigations against your cluster.")
    click.echo("     Press Ctrl+C to continue in local/BYOK mode (no cloud).")
    click.echo("")
    try:
        value = click.prompt("  Hexawyn Cloud token", hide_input=False, show_default=False)
        return value if isinstance(value, str) else None
    except (click.Abort, KeyboardInterrupt):
        return None


def x__prompt_token__mutmut_22() -> str | None:
    """Prompt for the Hexawyn Cloud token using hidden input."""
    click.echo("  ✨ A Cloud token unlocks AI investigations against your cluster.")
    click.echo("     Press Ctrl+C to continue in local/BYOK mode (no cloud).")
    click.echo("")
    try:
        value = click.prompt("  Hexawyn Cloud token", hide_input=True, show_default=True)
        return value if isinstance(value, str) else None
    except (click.Abort, KeyboardInterrupt):
        return None

mutants_x__prompt_token__mutmut['_mutmut_orig'] = x__prompt_token__mutmut_orig # type: ignore # mutmut generated
mutants_x__prompt_token__mutmut['x__prompt_token__mutmut_1'] = x__prompt_token__mutmut_1 # type: ignore # mutmut generated
mutants_x__prompt_token__mutmut['x__prompt_token__mutmut_2'] = x__prompt_token__mutmut_2 # type: ignore # mutmut generated
mutants_x__prompt_token__mutmut['x__prompt_token__mutmut_3'] = x__prompt_token__mutmut_3 # type: ignore # mutmut generated
mutants_x__prompt_token__mutmut['x__prompt_token__mutmut_4'] = x__prompt_token__mutmut_4 # type: ignore # mutmut generated
mutants_x__prompt_token__mutmut['x__prompt_token__mutmut_5'] = x__prompt_token__mutmut_5 # type: ignore # mutmut generated
mutants_x__prompt_token__mutmut['x__prompt_token__mutmut_6'] = x__prompt_token__mutmut_6 # type: ignore # mutmut generated
mutants_x__prompt_token__mutmut['x__prompt_token__mutmut_7'] = x__prompt_token__mutmut_7 # type: ignore # mutmut generated
mutants_x__prompt_token__mutmut['x__prompt_token__mutmut_8'] = x__prompt_token__mutmut_8 # type: ignore # mutmut generated
mutants_x__prompt_token__mutmut['x__prompt_token__mutmut_9'] = x__prompt_token__mutmut_9 # type: ignore # mutmut generated
mutants_x__prompt_token__mutmut['x__prompt_token__mutmut_10'] = x__prompt_token__mutmut_10 # type: ignore # mutmut generated
mutants_x__prompt_token__mutmut['x__prompt_token__mutmut_11'] = x__prompt_token__mutmut_11 # type: ignore # mutmut generated
mutants_x__prompt_token__mutmut['x__prompt_token__mutmut_12'] = x__prompt_token__mutmut_12 # type: ignore # mutmut generated
mutants_x__prompt_token__mutmut['x__prompt_token__mutmut_13'] = x__prompt_token__mutmut_13 # type: ignore # mutmut generated
mutants_x__prompt_token__mutmut['x__prompt_token__mutmut_14'] = x__prompt_token__mutmut_14 # type: ignore # mutmut generated
mutants_x__prompt_token__mutmut['x__prompt_token__mutmut_15'] = x__prompt_token__mutmut_15 # type: ignore # mutmut generated
mutants_x__prompt_token__mutmut['x__prompt_token__mutmut_16'] = x__prompt_token__mutmut_16 # type: ignore # mutmut generated
mutants_x__prompt_token__mutmut['x__prompt_token__mutmut_17'] = x__prompt_token__mutmut_17 # type: ignore # mutmut generated
mutants_x__prompt_token__mutmut['x__prompt_token__mutmut_18'] = x__prompt_token__mutmut_18 # type: ignore # mutmut generated
mutants_x__prompt_token__mutmut['x__prompt_token__mutmut_19'] = x__prompt_token__mutmut_19 # type: ignore # mutmut generated
mutants_x__prompt_token__mutmut['x__prompt_token__mutmut_20'] = x__prompt_token__mutmut_20 # type: ignore # mutmut generated
mutants_x__prompt_token__mutmut['x__prompt_token__mutmut_21'] = x__prompt_token__mutmut_21 # type: ignore # mutmut generated
mutants_x__prompt_token__mutmut['x__prompt_token__mutmut_22'] = x__prompt_token__mutmut_22 # type: ignore # mutmut generated
mutants_x__welcome__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__welcome__mutmut)
def _welcome() -> None:
    """Render a welcoming banner for `hexa start`."""
    from hexawyn.cli.presentation.feedback import header

    header()
    click.echo("  👋 Welcome to Hexawyn — your AI-powered Kubernetes assistant.")
    click.echo("")


def x__welcome__mutmut_orig() -> None:
    """Render a welcoming banner for `hexa start`."""
    from hexawyn.cli.presentation.feedback import header

    header()
    click.echo("  👋 Welcome to Hexawyn — your AI-powered Kubernetes assistant.")
    click.echo("")


def x__welcome__mutmut_1() -> None:
    """Render a welcoming banner for `hexa start`."""
    from hexawyn.cli.presentation.feedback import header

    header()
    click.echo(None)
    click.echo("")


def x__welcome__mutmut_2() -> None:
    """Render a welcoming banner for `hexa start`."""
    from hexawyn.cli.presentation.feedback import header

    header()
    click.echo("XX  👋 Welcome to Hexawyn — your AI-powered Kubernetes assistant.XX")
    click.echo("")


def x__welcome__mutmut_3() -> None:
    """Render a welcoming banner for `hexa start`."""
    from hexawyn.cli.presentation.feedback import header

    header()
    click.echo("  👋 welcome to hexawyn — your ai-powered kubernetes assistant.")
    click.echo("")


def x__welcome__mutmut_4() -> None:
    """Render a welcoming banner for `hexa start`."""
    from hexawyn.cli.presentation.feedback import header

    header()
    click.echo("  👋 WELCOME TO HEXAWYN — YOUR AI-POWERED KUBERNETES ASSISTANT.")
    click.echo("")


def x__welcome__mutmut_5() -> None:
    """Render a welcoming banner for `hexa start`."""
    from hexawyn.cli.presentation.feedback import header

    header()
    click.echo("  👋 Welcome to Hexawyn — your AI-powered Kubernetes assistant.")
    click.echo(None)


def x__welcome__mutmut_6() -> None:
    """Render a welcoming banner for `hexa start`."""
    from hexawyn.cli.presentation.feedback import header

    header()
    click.echo("  👋 Welcome to Hexawyn — your AI-powered Kubernetes assistant.")
    click.echo("XXXX")

mutants_x__welcome__mutmut['_mutmut_orig'] = x__welcome__mutmut_orig # type: ignore # mutmut generated
mutants_x__welcome__mutmut['x__welcome__mutmut_1'] = x__welcome__mutmut_1 # type: ignore # mutmut generated
mutants_x__welcome__mutmut['x__welcome__mutmut_2'] = x__welcome__mutmut_2 # type: ignore # mutmut generated
mutants_x__welcome__mutmut['x__welcome__mutmut_3'] = x__welcome__mutmut_3 # type: ignore # mutmut generated
mutants_x__welcome__mutmut['x__welcome__mutmut_4'] = x__welcome__mutmut_4 # type: ignore # mutmut generated
mutants_x__welcome__mutmut['x__welcome__mutmut_5'] = x__welcome__mutmut_5 # type: ignore # mutmut generated
mutants_x__welcome__mutmut['x__welcome__mutmut_6'] = x__welcome__mutmut_6 # type: ignore # mutmut generated


_register_start(app)

from hexawyn.cli.commands.auth_command import auth  # noqa: E402, I001
from hexawyn.cli.commands.cache_command import cache  # noqa: E402, I001
from hexawyn.cli.commands.claude_command import claude  # noqa: E402, I001
from hexawyn.cli.commands.cluster_command import cluster  # noqa: E402, I001
from hexawyn.cli.commands.codex_command import codex  # noqa: E402, I001
from hexawyn.cli.commands.config_command import config  # noqa: E402, I001
from hexawyn.cli.commands.cursor_command import cursor  # noqa: E402, I001
from hexawyn.cli.commands.db_command import db  # noqa: E402, I001
from hexawyn.cli.commands.deepseek_command import deepseek  # noqa: E402, I001
from hexawyn.cli.commands.gemini_command import gemini  # noqa: E402, I001
from hexawyn.cli.commands.opencode_command import opencode  # noqa: E402, I001
from hexawyn.cli.commands.quota_command import quota  # noqa: E402, I001
from hexawyn.cli.commands.schedule_command import schedule  # noqa: E402, I001
from hexawyn.cli.commands.slack_command import slack  # noqa: E402, I001
from hexawyn.cli.commands.update_command import update, update_check, version  # noqa: E402, I001
from hexawyn.cli.commands.uninstall_command import uninstall  # noqa: E402, I001

app.add_command(auth)
app.add_command(config)
app.add_command(quota)
app.add_command(cluster)
app.add_command(db)
app.add_command(cache)
app.add_command(schedule)
app.add_command(slack)
app.add_command(claude)
app.add_command(codex)
app.add_command(opencode)
app.add_command(cursor)
app.add_command(gemini)
app.add_command(deepseek)
app.add_command(update)
app.add_command(update_check)
app.add_command(version)
app.add_command(uninstall)


if __name__ == "__main__":
    app()
