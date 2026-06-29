import re

from hexawyn.adapters.primary.slack.slack_chat_adapter import SlackChatAdapter


def handle_slack_event(event: dict[str, object]) -> dict[str, object]:
    """
    Handle incoming Slack event.

    Supports:
    - url_verification: respond with challenge (Slack app setup)
    - app_mention: user mentions @hexawyn → run investigation
    """
    event_type = event.get("type")

    if event_type == "url_verification":
        return {"challenge": event.get("challenge", "")}

    if event_type == "event_callback":
        inner = event.get("event", {})
        if not isinstance(inner, dict):
            return {"ok": True}
        if inner.get("type") == "app_mention":
            return _handle_app_mention(inner)

    return {"ok": True}


def _handle_app_mention(inner: dict[str, object]) -> dict[str, object]:
    text = str(inner.get("text", ""))
    query = re.sub(r"<@[A-Z0-9]+>", "", text).strip()
    channel_id = str(inner.get("channel", ""))
    thread_ts = inner.get("thread_ts") or inner.get("ts")

    cluster_name = _get_active_cluster_name()
    adapter = SlackChatAdapter()
    response = adapter.handle_message(
        query=query,
        cluster_name=cluster_name,
        channel_id=channel_id,
        thread_ts=str(thread_ts) if thread_ts else None,
    )
    return {"response": response, "channel": channel_id}


def _get_active_cluster_name() -> str:
    try:
        from hexawyn.infrastructure.config.kubeconfig_reader import get_active_context

        ctx = get_active_context()
        if ctx is not None and ctx.get("name"):
            return str(ctx.get("name"))
    except Exception:
        pass

    try:
        import subprocess

        result = subprocess.run(
            ["kubectl", "config", "current-context"],
            capture_output=True,
            text=True,
            timeout=5,
        )
        if result.returncode == 0 and result.stdout.strip():
            return result.stdout.strip()
    except Exception:
        pass

    return "unknown"
