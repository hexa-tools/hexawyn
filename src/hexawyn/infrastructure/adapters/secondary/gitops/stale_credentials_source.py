from __future__ import annotations

import datetime

from hexawyn.application.ports.driven.stale_credentials_port import StaleCredentialRaw
from kubernetes import client, config


class EmptyStaleCredentialsSource:
    def fetch_stale_credentials(self, min_days: int) -> list[StaleCredentialRaw]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()
            secrets = v1.list_secret_for_all_namespaces()
            cutoff = datetime.datetime.now(datetime.UTC) - datetime.timedelta(days=min_days)

            result: list[StaleCredentialRaw] = []
            for secret in secrets.items:
                if not secret.metadata:
                    continue
                created = secret.metadata.creation_timestamp
                if created and created.replace(tzinfo=datetime.UTC) < cutoff:
                    result.append(
                        StaleCredentialRaw(  # type: ignore
                            name=secret.metadata.name or "",
                            namespace=secret.metadata.namespace or "",
                            age_days=min_days,
                            type=secret.type or "Opaque",
                        )
                    )
            return result
        except Exception:
            return []
