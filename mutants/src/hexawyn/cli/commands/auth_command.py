"""hexa auth — manage hexawyn cloud authentication and licensing."""

from datetime import UTC, datetime

import click
import httpx

from hexawyn.infrastructure.config.config_manager import load_config, save_config
from hexawyn.infrastructure.license.license_reader import LICENSE_KEY_PATH, read_license_state

HEXA_CLOUD_BASE_URL = "https://api.hexawyn.com"


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@click.group()
def auth() -> None:
    """Manage hexawyn cloud license and authentication."""


@auth.command()
@click.argument("token")
@click.option(
    "--endpoint",
    default=HEXA_CLOUD_BASE_URL,
    help="hexa-cloud API endpoint",
    envvar="HEXAWYN_CLOUD_ENDPOINT",
)
def set_token(token: str, endpoint: str) -> None:
    """Activate a license by providing your hexawyn API key.

    TOKEN is the API key received by email after subscribing.
    """
    token = token.strip()

    url = f"{endpoint}/api/v1/license/activate"
    try:
        response = _activate_license(url, token)
    except httpx.ConnectError:
        click.echo(f"❌ Failed to connect to {endpoint}. Is the API reachable?", err=True)
        raise SystemExit(1)

    if response.status_code != 200:  # noqa: PLR2004
        detail = "Unknown error"
        try:
            detail = response.json().get("detail", detail)
        except Exception:
            pass
        click.echo(f"❌ License activation failed: {detail}", err=True)
        raise SystemExit(1)

    data = response.json()
    jwt_token = data.get("token", "")
    plan = data.get("plan", "unknown")
    expires_at = data.get("expires_at", "")

    LICENSE_KEY_PATH.parent.mkdir(parents=True, exist_ok=True)
    LICENSE_KEY_PATH.write_text(jwt_token)

    config = load_config()
    config["hexawyn_token"] = token
    config["hexawyn_token_prefix"] = token[: min(len(token), 16)]
    save_config(config)

    click.echo(f"✅ License activated — Plan: {plan}")
    click.echo(f"   Token:  {token[:16]}...")
    click.echo(f"   Expires: {_format_expiry(expires_at)}")


@auth.command()
def status() -> None:
    """Show current license activation status."""
    state_info = read_license_state()

    if state_info.state == "missing":
        click.echo("❌ License not configured. Run `hexa auth set-token <TOKEN>` to activate.")
        return

    if state_info.state == "invalid":
        click.echo("❌ Could not read license data.")
        return

    if state_info.state == "expired":
        click.echo(f"⚠ License expired — Plan: {state_info.plan.title()}")
        click.echo("   Run `hexa auth set-token <TOKEN>` to renew.")
        return

    click.echo(f"✅ License active — Plan: {state_info.plan.title()}")
    click.echo(f"   Expires: {state_info.expiry_date} ({state_info.days_remaining} days)")
mutants_x__activate_license__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__activate_license__mutmut)
def _activate_license(url: str, token: str) -> httpx.Response:
    """Call the hexa-cloud license activation endpoint (synchronous)."""
    import asyncio

    async def _post() -> httpx.Response:
        from hexawyn.infrastructure.config.machine_id import get_machine_id

        machine_id = get_machine_id()
        async with httpx.AsyncClient(timeout=10) as client:
            return await client.post(
                url,
                json={
                    "api_key": token,
                    "machine_id": machine_id,
                    "client_version": "1.0.0",
                },
            )

    return asyncio.run(_post())


def x__activate_license__mutmut_orig(url: str, token: str) -> httpx.Response:
    """Call the hexa-cloud license activation endpoint (synchronous)."""
    import asyncio

    async def _post() -> httpx.Response:
        from hexawyn.infrastructure.config.machine_id import get_machine_id

        machine_id = get_machine_id()
        async with httpx.AsyncClient(timeout=10) as client:
            return await client.post(
                url,
                json={
                    "api_key": token,
                    "machine_id": machine_id,
                    "client_version": "1.0.0",
                },
            )

    return asyncio.run(_post())


def x__activate_license__mutmut_1(url: str, token: str) -> httpx.Response:
    """Call the hexa-cloud license activation endpoint (synchronous)."""
    import asyncio

    async def _post() -> httpx.Response:
        from hexawyn.infrastructure.config.machine_id import get_machine_id

        machine_id = None
        async with httpx.AsyncClient(timeout=10) as client:
            return await client.post(
                url,
                json={
                    "api_key": token,
                    "machine_id": machine_id,
                    "client_version": "1.0.0",
                },
            )

    return asyncio.run(_post())


def x__activate_license__mutmut_2(url: str, token: str) -> httpx.Response:
    """Call the hexa-cloud license activation endpoint (synchronous)."""
    import asyncio

    async def _post() -> httpx.Response:
        from hexawyn.infrastructure.config.machine_id import get_machine_id

        machine_id = get_machine_id()
        async with httpx.AsyncClient(timeout=None) as client:
            return await client.post(
                url,
                json={
                    "api_key": token,
                    "machine_id": machine_id,
                    "client_version": "1.0.0",
                },
            )

    return asyncio.run(_post())


def x__activate_license__mutmut_3(url: str, token: str) -> httpx.Response:
    """Call the hexa-cloud license activation endpoint (synchronous)."""
    import asyncio

    async def _post() -> httpx.Response:
        from hexawyn.infrastructure.config.machine_id import get_machine_id

        machine_id = get_machine_id()
        async with httpx.AsyncClient(timeout=11) as client:
            return await client.post(
                url,
                json={
                    "api_key": token,
                    "machine_id": machine_id,
                    "client_version": "1.0.0",
                },
            )

    return asyncio.run(_post())


def x__activate_license__mutmut_4(url: str, token: str) -> httpx.Response:
    """Call the hexa-cloud license activation endpoint (synchronous)."""
    import asyncio

    async def _post() -> httpx.Response:
        from hexawyn.infrastructure.config.machine_id import get_machine_id

        machine_id = get_machine_id()
        async with httpx.AsyncClient(timeout=10) as client:
            return await client.post(
                None,
                json={
                    "api_key": token,
                    "machine_id": machine_id,
                    "client_version": "1.0.0",
                },
            )

    return asyncio.run(_post())


def x__activate_license__mutmut_5(url: str, token: str) -> httpx.Response:
    """Call the hexa-cloud license activation endpoint (synchronous)."""
    import asyncio

    async def _post() -> httpx.Response:
        from hexawyn.infrastructure.config.machine_id import get_machine_id

        machine_id = get_machine_id()
        async with httpx.AsyncClient(timeout=10) as client:
            return await client.post(
                url,
                json=None,
            )

    return asyncio.run(_post())


def x__activate_license__mutmut_6(url: str, token: str) -> httpx.Response:
    """Call the hexa-cloud license activation endpoint (synchronous)."""
    import asyncio

    async def _post() -> httpx.Response:
        from hexawyn.infrastructure.config.machine_id import get_machine_id

        machine_id = get_machine_id()
        async with httpx.AsyncClient(timeout=10) as client:
            return await client.post(
                json={
                    "api_key": token,
                    "machine_id": machine_id,
                    "client_version": "1.0.0",
                },
            )

    return asyncio.run(_post())


def x__activate_license__mutmut_7(url: str, token: str) -> httpx.Response:
    """Call the hexa-cloud license activation endpoint (synchronous)."""
    import asyncio

    async def _post() -> httpx.Response:
        from hexawyn.infrastructure.config.machine_id import get_machine_id

        machine_id = get_machine_id()
        async with httpx.AsyncClient(timeout=10) as client:
            return await client.post(
                url,
                )

    return asyncio.run(_post())


def x__activate_license__mutmut_8(url: str, token: str) -> httpx.Response:
    """Call the hexa-cloud license activation endpoint (synchronous)."""
    import asyncio

    async def _post() -> httpx.Response:
        from hexawyn.infrastructure.config.machine_id import get_machine_id

        machine_id = get_machine_id()
        async with httpx.AsyncClient(timeout=10) as client:
            return await client.post(
                url,
                json={
                    "XXapi_keyXX": token,
                    "machine_id": machine_id,
                    "client_version": "1.0.0",
                },
            )

    return asyncio.run(_post())


def x__activate_license__mutmut_9(url: str, token: str) -> httpx.Response:
    """Call the hexa-cloud license activation endpoint (synchronous)."""
    import asyncio

    async def _post() -> httpx.Response:
        from hexawyn.infrastructure.config.machine_id import get_machine_id

        machine_id = get_machine_id()
        async with httpx.AsyncClient(timeout=10) as client:
            return await client.post(
                url,
                json={
                    "API_KEY": token,
                    "machine_id": machine_id,
                    "client_version": "1.0.0",
                },
            )

    return asyncio.run(_post())


def x__activate_license__mutmut_10(url: str, token: str) -> httpx.Response:
    """Call the hexa-cloud license activation endpoint (synchronous)."""
    import asyncio

    async def _post() -> httpx.Response:
        from hexawyn.infrastructure.config.machine_id import get_machine_id

        machine_id = get_machine_id()
        async with httpx.AsyncClient(timeout=10) as client:
            return await client.post(
                url,
                json={
                    "api_key": token,
                    "XXmachine_idXX": machine_id,
                    "client_version": "1.0.0",
                },
            )

    return asyncio.run(_post())


def x__activate_license__mutmut_11(url: str, token: str) -> httpx.Response:
    """Call the hexa-cloud license activation endpoint (synchronous)."""
    import asyncio

    async def _post() -> httpx.Response:
        from hexawyn.infrastructure.config.machine_id import get_machine_id

        machine_id = get_machine_id()
        async with httpx.AsyncClient(timeout=10) as client:
            return await client.post(
                url,
                json={
                    "api_key": token,
                    "MACHINE_ID": machine_id,
                    "client_version": "1.0.0",
                },
            )

    return asyncio.run(_post())


def x__activate_license__mutmut_12(url: str, token: str) -> httpx.Response:
    """Call the hexa-cloud license activation endpoint (synchronous)."""
    import asyncio

    async def _post() -> httpx.Response:
        from hexawyn.infrastructure.config.machine_id import get_machine_id

        machine_id = get_machine_id()
        async with httpx.AsyncClient(timeout=10) as client:
            return await client.post(
                url,
                json={
                    "api_key": token,
                    "machine_id": machine_id,
                    "XXclient_versionXX": "1.0.0",
                },
            )

    return asyncio.run(_post())


def x__activate_license__mutmut_13(url: str, token: str) -> httpx.Response:
    """Call the hexa-cloud license activation endpoint (synchronous)."""
    import asyncio

    async def _post() -> httpx.Response:
        from hexawyn.infrastructure.config.machine_id import get_machine_id

        machine_id = get_machine_id()
        async with httpx.AsyncClient(timeout=10) as client:
            return await client.post(
                url,
                json={
                    "api_key": token,
                    "machine_id": machine_id,
                    "CLIENT_VERSION": "1.0.0",
                },
            )

    return asyncio.run(_post())


def x__activate_license__mutmut_14(url: str, token: str) -> httpx.Response:
    """Call the hexa-cloud license activation endpoint (synchronous)."""
    import asyncio

    async def _post() -> httpx.Response:
        from hexawyn.infrastructure.config.machine_id import get_machine_id

        machine_id = get_machine_id()
        async with httpx.AsyncClient(timeout=10) as client:
            return await client.post(
                url,
                json={
                    "api_key": token,
                    "machine_id": machine_id,
                    "client_version": "XX1.0.0XX",
                },
            )

    return asyncio.run(_post())


def x__activate_license__mutmut_15(url: str, token: str) -> httpx.Response:
    """Call the hexa-cloud license activation endpoint (synchronous)."""
    import asyncio

    async def _post() -> httpx.Response:
        from hexawyn.infrastructure.config.machine_id import get_machine_id

        machine_id = get_machine_id()
        async with httpx.AsyncClient(timeout=10) as client:
            return await client.post(
                url,
                json={
                    "api_key": token,
                    "machine_id": machine_id,
                    "client_version": "1.0.0",
                },
            )

    return asyncio.run(None)

mutants_x__activate_license__mutmut['_mutmut_orig'] = x__activate_license__mutmut_orig # type: ignore # mutmut generated
mutants_x__activate_license__mutmut['x__activate_license__mutmut_1'] = x__activate_license__mutmut_1 # type: ignore # mutmut generated
mutants_x__activate_license__mutmut['x__activate_license__mutmut_2'] = x__activate_license__mutmut_2 # type: ignore # mutmut generated
mutants_x__activate_license__mutmut['x__activate_license__mutmut_3'] = x__activate_license__mutmut_3 # type: ignore # mutmut generated
mutants_x__activate_license__mutmut['x__activate_license__mutmut_4'] = x__activate_license__mutmut_4 # type: ignore # mutmut generated
mutants_x__activate_license__mutmut['x__activate_license__mutmut_5'] = x__activate_license__mutmut_5 # type: ignore # mutmut generated
mutants_x__activate_license__mutmut['x__activate_license__mutmut_6'] = x__activate_license__mutmut_6 # type: ignore # mutmut generated
mutants_x__activate_license__mutmut['x__activate_license__mutmut_7'] = x__activate_license__mutmut_7 # type: ignore # mutmut generated
mutants_x__activate_license__mutmut['x__activate_license__mutmut_8'] = x__activate_license__mutmut_8 # type: ignore # mutmut generated
mutants_x__activate_license__mutmut['x__activate_license__mutmut_9'] = x__activate_license__mutmut_9 # type: ignore # mutmut generated
mutants_x__activate_license__mutmut['x__activate_license__mutmut_10'] = x__activate_license__mutmut_10 # type: ignore # mutmut generated
mutants_x__activate_license__mutmut['x__activate_license__mutmut_11'] = x__activate_license__mutmut_11 # type: ignore # mutmut generated
mutants_x__activate_license__mutmut['x__activate_license__mutmut_12'] = x__activate_license__mutmut_12 # type: ignore # mutmut generated
mutants_x__activate_license__mutmut['x__activate_license__mutmut_13'] = x__activate_license__mutmut_13 # type: ignore # mutmut generated
mutants_x__activate_license__mutmut['x__activate_license__mutmut_14'] = x__activate_license__mutmut_14 # type: ignore # mutmut generated
mutants_x__activate_license__mutmut['x__activate_license__mutmut_15'] = x__activate_license__mutmut_15 # type: ignore # mutmut generated
mutants_x__format_expiry__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__format_expiry__mutmut)
def _format_expiry(expires_at: str) -> str:
    if not expires_at:
        return "unknown"
    try:
        if expires_at.isdigit():
            dt = datetime.fromtimestamp(int(expires_at), tz=UTC)
        else:
            dt = datetime.fromisoformat(expires_at.replace("Z", "+00:00"))
        days = (dt - datetime.now(UTC)).days
        return f"{dt.strftime('%d %b %Y')} ({days} days)"
    except (ValueError, OverflowError):
        return expires_at


def x__format_expiry__mutmut_orig(expires_at: str) -> str:
    if not expires_at:
        return "unknown"
    try:
        if expires_at.isdigit():
            dt = datetime.fromtimestamp(int(expires_at), tz=UTC)
        else:
            dt = datetime.fromisoformat(expires_at.replace("Z", "+00:00"))
        days = (dt - datetime.now(UTC)).days
        return f"{dt.strftime('%d %b %Y')} ({days} days)"
    except (ValueError, OverflowError):
        return expires_at


def x__format_expiry__mutmut_1(expires_at: str) -> str:
    if expires_at:
        return "unknown"
    try:
        if expires_at.isdigit():
            dt = datetime.fromtimestamp(int(expires_at), tz=UTC)
        else:
            dt = datetime.fromisoformat(expires_at.replace("Z", "+00:00"))
        days = (dt - datetime.now(UTC)).days
        return f"{dt.strftime('%d %b %Y')} ({days} days)"
    except (ValueError, OverflowError):
        return expires_at


def x__format_expiry__mutmut_2(expires_at: str) -> str:
    if not expires_at:
        return "XXunknownXX"
    try:
        if expires_at.isdigit():
            dt = datetime.fromtimestamp(int(expires_at), tz=UTC)
        else:
            dt = datetime.fromisoformat(expires_at.replace("Z", "+00:00"))
        days = (dt - datetime.now(UTC)).days
        return f"{dt.strftime('%d %b %Y')} ({days} days)"
    except (ValueError, OverflowError):
        return expires_at


def x__format_expiry__mutmut_3(expires_at: str) -> str:
    if not expires_at:
        return "UNKNOWN"
    try:
        if expires_at.isdigit():
            dt = datetime.fromtimestamp(int(expires_at), tz=UTC)
        else:
            dt = datetime.fromisoformat(expires_at.replace("Z", "+00:00"))
        days = (dt - datetime.now(UTC)).days
        return f"{dt.strftime('%d %b %Y')} ({days} days)"
    except (ValueError, OverflowError):
        return expires_at


def x__format_expiry__mutmut_4(expires_at: str) -> str:
    if not expires_at:
        return "unknown"
    try:
        if expires_at.isdigit():
            dt = None
        else:
            dt = datetime.fromisoformat(expires_at.replace("Z", "+00:00"))
        days = (dt - datetime.now(UTC)).days
        return f"{dt.strftime('%d %b %Y')} ({days} days)"
    except (ValueError, OverflowError):
        return expires_at


def x__format_expiry__mutmut_5(expires_at: str) -> str:
    if not expires_at:
        return "unknown"
    try:
        if expires_at.isdigit():
            dt = datetime.fromtimestamp(None, tz=UTC)
        else:
            dt = datetime.fromisoformat(expires_at.replace("Z", "+00:00"))
        days = (dt - datetime.now(UTC)).days
        return f"{dt.strftime('%d %b %Y')} ({days} days)"
    except (ValueError, OverflowError):
        return expires_at


def x__format_expiry__mutmut_6(expires_at: str) -> str:
    if not expires_at:
        return "unknown"
    try:
        if expires_at.isdigit():
            dt = datetime.fromtimestamp(int(expires_at), tz=None)
        else:
            dt = datetime.fromisoformat(expires_at.replace("Z", "+00:00"))
        days = (dt - datetime.now(UTC)).days
        return f"{dt.strftime('%d %b %Y')} ({days} days)"
    except (ValueError, OverflowError):
        return expires_at


def x__format_expiry__mutmut_7(expires_at: str) -> str:
    if not expires_at:
        return "unknown"
    try:
        if expires_at.isdigit():
            dt = datetime.fromtimestamp(tz=UTC)
        else:
            dt = datetime.fromisoformat(expires_at.replace("Z", "+00:00"))
        days = (dt - datetime.now(UTC)).days
        return f"{dt.strftime('%d %b %Y')} ({days} days)"
    except (ValueError, OverflowError):
        return expires_at


def x__format_expiry__mutmut_8(expires_at: str) -> str:
    if not expires_at:
        return "unknown"
    try:
        if expires_at.isdigit():
            dt = datetime.fromtimestamp(int(expires_at), )
        else:
            dt = datetime.fromisoformat(expires_at.replace("Z", "+00:00"))
        days = (dt - datetime.now(UTC)).days
        return f"{dt.strftime('%d %b %Y')} ({days} days)"
    except (ValueError, OverflowError):
        return expires_at


def x__format_expiry__mutmut_9(expires_at: str) -> str:
    if not expires_at:
        return "unknown"
    try:
        if expires_at.isdigit():
            dt = datetime.fromtimestamp(int(None), tz=UTC)
        else:
            dt = datetime.fromisoformat(expires_at.replace("Z", "+00:00"))
        days = (dt - datetime.now(UTC)).days
        return f"{dt.strftime('%d %b %Y')} ({days} days)"
    except (ValueError, OverflowError):
        return expires_at


def x__format_expiry__mutmut_10(expires_at: str) -> str:
    if not expires_at:
        return "unknown"
    try:
        if expires_at.isdigit():
            dt = datetime.fromtimestamp(int(expires_at), tz=UTC)
        else:
            dt = None
        days = (dt - datetime.now(UTC)).days
        return f"{dt.strftime('%d %b %Y')} ({days} days)"
    except (ValueError, OverflowError):
        return expires_at


def x__format_expiry__mutmut_11(expires_at: str) -> str:
    if not expires_at:
        return "unknown"
    try:
        if expires_at.isdigit():
            dt = datetime.fromtimestamp(int(expires_at), tz=UTC)
        else:
            dt = datetime.fromisoformat(None)
        days = (dt - datetime.now(UTC)).days
        return f"{dt.strftime('%d %b %Y')} ({days} days)"
    except (ValueError, OverflowError):
        return expires_at


def x__format_expiry__mutmut_12(expires_at: str) -> str:
    if not expires_at:
        return "unknown"
    try:
        if expires_at.isdigit():
            dt = datetime.fromtimestamp(int(expires_at), tz=UTC)
        else:
            dt = datetime.fromisoformat(expires_at.replace(None, "+00:00"))
        days = (dt - datetime.now(UTC)).days
        return f"{dt.strftime('%d %b %Y')} ({days} days)"
    except (ValueError, OverflowError):
        return expires_at


def x__format_expiry__mutmut_13(expires_at: str) -> str:
    if not expires_at:
        return "unknown"
    try:
        if expires_at.isdigit():
            dt = datetime.fromtimestamp(int(expires_at), tz=UTC)
        else:
            dt = datetime.fromisoformat(expires_at.replace("Z", None))
        days = (dt - datetime.now(UTC)).days
        return f"{dt.strftime('%d %b %Y')} ({days} days)"
    except (ValueError, OverflowError):
        return expires_at


def x__format_expiry__mutmut_14(expires_at: str) -> str:
    if not expires_at:
        return "unknown"
    try:
        if expires_at.isdigit():
            dt = datetime.fromtimestamp(int(expires_at), tz=UTC)
        else:
            dt = datetime.fromisoformat(expires_at.replace("+00:00"))
        days = (dt - datetime.now(UTC)).days
        return f"{dt.strftime('%d %b %Y')} ({days} days)"
    except (ValueError, OverflowError):
        return expires_at


def x__format_expiry__mutmut_15(expires_at: str) -> str:
    if not expires_at:
        return "unknown"
    try:
        if expires_at.isdigit():
            dt = datetime.fromtimestamp(int(expires_at), tz=UTC)
        else:
            dt = datetime.fromisoformat(expires_at.replace("Z", ))
        days = (dt - datetime.now(UTC)).days
        return f"{dt.strftime('%d %b %Y')} ({days} days)"
    except (ValueError, OverflowError):
        return expires_at


def x__format_expiry__mutmut_16(expires_at: str) -> str:
    if not expires_at:
        return "unknown"
    try:
        if expires_at.isdigit():
            dt = datetime.fromtimestamp(int(expires_at), tz=UTC)
        else:
            dt = datetime.fromisoformat(expires_at.replace("XXZXX", "+00:00"))
        days = (dt - datetime.now(UTC)).days
        return f"{dt.strftime('%d %b %Y')} ({days} days)"
    except (ValueError, OverflowError):
        return expires_at


def x__format_expiry__mutmut_17(expires_at: str) -> str:
    if not expires_at:
        return "unknown"
    try:
        if expires_at.isdigit():
            dt = datetime.fromtimestamp(int(expires_at), tz=UTC)
        else:
            dt = datetime.fromisoformat(expires_at.replace("z", "+00:00"))
        days = (dt - datetime.now(UTC)).days
        return f"{dt.strftime('%d %b %Y')} ({days} days)"
    except (ValueError, OverflowError):
        return expires_at


def x__format_expiry__mutmut_18(expires_at: str) -> str:
    if not expires_at:
        return "unknown"
    try:
        if expires_at.isdigit():
            dt = datetime.fromtimestamp(int(expires_at), tz=UTC)
        else:
            dt = datetime.fromisoformat(expires_at.replace("Z", "XX+00:00XX"))
        days = (dt - datetime.now(UTC)).days
        return f"{dt.strftime('%d %b %Y')} ({days} days)"
    except (ValueError, OverflowError):
        return expires_at


def x__format_expiry__mutmut_19(expires_at: str) -> str:
    if not expires_at:
        return "unknown"
    try:
        if expires_at.isdigit():
            dt = datetime.fromtimestamp(int(expires_at), tz=UTC)
        else:
            dt = datetime.fromisoformat(expires_at.replace("Z", "+00:00"))
        days = None
        return f"{dt.strftime('%d %b %Y')} ({days} days)"
    except (ValueError, OverflowError):
        return expires_at


def x__format_expiry__mutmut_20(expires_at: str) -> str:
    if not expires_at:
        return "unknown"
    try:
        if expires_at.isdigit():
            dt = datetime.fromtimestamp(int(expires_at), tz=UTC)
        else:
            dt = datetime.fromisoformat(expires_at.replace("Z", "+00:00"))
        days = (dt + datetime.now(UTC)).days
        return f"{dt.strftime('%d %b %Y')} ({days} days)"
    except (ValueError, OverflowError):
        return expires_at


def x__format_expiry__mutmut_21(expires_at: str) -> str:
    if not expires_at:
        return "unknown"
    try:
        if expires_at.isdigit():
            dt = datetime.fromtimestamp(int(expires_at), tz=UTC)
        else:
            dt = datetime.fromisoformat(expires_at.replace("Z", "+00:00"))
        days = (dt - datetime.now(None)).days
        return f"{dt.strftime('%d %b %Y')} ({days} days)"
    except (ValueError, OverflowError):
        return expires_at


def x__format_expiry__mutmut_22(expires_at: str) -> str:
    if not expires_at:
        return "unknown"
    try:
        if expires_at.isdigit():
            dt = datetime.fromtimestamp(int(expires_at), tz=UTC)
        else:
            dt = datetime.fromisoformat(expires_at.replace("Z", "+00:00"))
        days = (dt - datetime.now(UTC)).days
        return f"{dt.strftime(None)} ({days} days)"
    except (ValueError, OverflowError):
        return expires_at


def x__format_expiry__mutmut_23(expires_at: str) -> str:
    if not expires_at:
        return "unknown"
    try:
        if expires_at.isdigit():
            dt = datetime.fromtimestamp(int(expires_at), tz=UTC)
        else:
            dt = datetime.fromisoformat(expires_at.replace("Z", "+00:00"))
        days = (dt - datetime.now(UTC)).days
        return f"{dt.strftime('XX%d %b %YXX')} ({days} days)"
    except (ValueError, OverflowError):
        return expires_at


def x__format_expiry__mutmut_24(expires_at: str) -> str:
    if not expires_at:
        return "unknown"
    try:
        if expires_at.isdigit():
            dt = datetime.fromtimestamp(int(expires_at), tz=UTC)
        else:
            dt = datetime.fromisoformat(expires_at.replace("Z", "+00:00"))
        days = (dt - datetime.now(UTC)).days
        return f"{dt.strftime('%d %b %y')} ({days} days)"
    except (ValueError, OverflowError):
        return expires_at


def x__format_expiry__mutmut_25(expires_at: str) -> str:
    if not expires_at:
        return "unknown"
    try:
        if expires_at.isdigit():
            dt = datetime.fromtimestamp(int(expires_at), tz=UTC)
        else:
            dt = datetime.fromisoformat(expires_at.replace("Z", "+00:00"))
        days = (dt - datetime.now(UTC)).days
        return f"{dt.strftime('%D %B %Y')} ({days} days)"
    except (ValueError, OverflowError):
        return expires_at

mutants_x__format_expiry__mutmut['_mutmut_orig'] = x__format_expiry__mutmut_orig # type: ignore # mutmut generated
mutants_x__format_expiry__mutmut['x__format_expiry__mutmut_1'] = x__format_expiry__mutmut_1 # type: ignore # mutmut generated
mutants_x__format_expiry__mutmut['x__format_expiry__mutmut_2'] = x__format_expiry__mutmut_2 # type: ignore # mutmut generated
mutants_x__format_expiry__mutmut['x__format_expiry__mutmut_3'] = x__format_expiry__mutmut_3 # type: ignore # mutmut generated
mutants_x__format_expiry__mutmut['x__format_expiry__mutmut_4'] = x__format_expiry__mutmut_4 # type: ignore # mutmut generated
mutants_x__format_expiry__mutmut['x__format_expiry__mutmut_5'] = x__format_expiry__mutmut_5 # type: ignore # mutmut generated
mutants_x__format_expiry__mutmut['x__format_expiry__mutmut_6'] = x__format_expiry__mutmut_6 # type: ignore # mutmut generated
mutants_x__format_expiry__mutmut['x__format_expiry__mutmut_7'] = x__format_expiry__mutmut_7 # type: ignore # mutmut generated
mutants_x__format_expiry__mutmut['x__format_expiry__mutmut_8'] = x__format_expiry__mutmut_8 # type: ignore # mutmut generated
mutants_x__format_expiry__mutmut['x__format_expiry__mutmut_9'] = x__format_expiry__mutmut_9 # type: ignore # mutmut generated
mutants_x__format_expiry__mutmut['x__format_expiry__mutmut_10'] = x__format_expiry__mutmut_10 # type: ignore # mutmut generated
mutants_x__format_expiry__mutmut['x__format_expiry__mutmut_11'] = x__format_expiry__mutmut_11 # type: ignore # mutmut generated
mutants_x__format_expiry__mutmut['x__format_expiry__mutmut_12'] = x__format_expiry__mutmut_12 # type: ignore # mutmut generated
mutants_x__format_expiry__mutmut['x__format_expiry__mutmut_13'] = x__format_expiry__mutmut_13 # type: ignore # mutmut generated
mutants_x__format_expiry__mutmut['x__format_expiry__mutmut_14'] = x__format_expiry__mutmut_14 # type: ignore # mutmut generated
mutants_x__format_expiry__mutmut['x__format_expiry__mutmut_15'] = x__format_expiry__mutmut_15 # type: ignore # mutmut generated
mutants_x__format_expiry__mutmut['x__format_expiry__mutmut_16'] = x__format_expiry__mutmut_16 # type: ignore # mutmut generated
mutants_x__format_expiry__mutmut['x__format_expiry__mutmut_17'] = x__format_expiry__mutmut_17 # type: ignore # mutmut generated
mutants_x__format_expiry__mutmut['x__format_expiry__mutmut_18'] = x__format_expiry__mutmut_18 # type: ignore # mutmut generated
mutants_x__format_expiry__mutmut['x__format_expiry__mutmut_19'] = x__format_expiry__mutmut_19 # type: ignore # mutmut generated
mutants_x__format_expiry__mutmut['x__format_expiry__mutmut_20'] = x__format_expiry__mutmut_20 # type: ignore # mutmut generated
mutants_x__format_expiry__mutmut['x__format_expiry__mutmut_21'] = x__format_expiry__mutmut_21 # type: ignore # mutmut generated
mutants_x__format_expiry__mutmut['x__format_expiry__mutmut_22'] = x__format_expiry__mutmut_22 # type: ignore # mutmut generated
mutants_x__format_expiry__mutmut['x__format_expiry__mutmut_23'] = x__format_expiry__mutmut_23 # type: ignore # mutmut generated
mutants_x__format_expiry__mutmut['x__format_expiry__mutmut_24'] = x__format_expiry__mutmut_24 # type: ignore # mutmut generated
mutants_x__format_expiry__mutmut['x__format_expiry__mutmut_25'] = x__format_expiry__mutmut_25 # type: ignore # mutmut generated


@auth.command()
def account() -> None:
    """Open the subscription management portal in your browser."""
    import webbrowser

    from hexawyn.infrastructure.config.config_manager import load_config

    config = load_config()
    token = config.get("hexawyn_token")

    if not token:
        click.echo(
            "❌ No license configured. Run `hexa auth set-token <TOKEN>` first.",
            err=True,
        )
        raise SystemExit(1)

    import httpx

    try:
        resp = httpx.post(
            "https://api.hexawyn.com/api/v1/billing/portal",
            json={"api_key": token},
            timeout=10,
        )
    except httpx.ConnectError:
        click.echo("❌ Cannot reach hexa-cloud. Visit polar.sh/purchases directly.")
        raise SystemExit(1)

    if resp.status_code != 200:  # noqa: PLR2004
        if resp.status_code == 404:  # noqa: PLR2004
            click.echo(
                "❌ Portal not available yet. Visit [link]https://polar.sh/purchases/subscriptions[/link]"
            )
        else:
            detail = "Unknown error"
            try:
                detail = resp.json().get("detail", detail)
            except Exception:
                pass
            click.echo(f"❌ {detail}")
        raise SystemExit(1)

    url = resp.json().get("url", "")
    if not url:
        click.echo("❌ No portal URL returned.", err=True)
        raise SystemExit(1)

    click.echo(f"Opening subscription portal: {url}")
    webbrowser.open(url)
