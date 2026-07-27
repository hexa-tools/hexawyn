from dataclasses import dataclass


@dataclass(frozen=True)
class ChatSlackCommand:
    query: str
    cluster_name: str
    channel_id: str
    thread_ts: str | None = None
