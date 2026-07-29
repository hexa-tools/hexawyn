"""hexa auth — manage hexawyn cloud authentication and licensing."""

from datetime import UTC, datetime

import click
import httpx

from hexawyn.infrastructure.config.config_manager import load_config, save_config
from hexawyn.infrastructure.license.license_reader import LICENSE_KEY_PATH, read_license_state

HEXA_CLOUD_BASE_URL = "https://api.hexawyn.com"


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
