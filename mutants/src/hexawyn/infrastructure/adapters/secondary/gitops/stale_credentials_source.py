from __future__ import annotations

import datetime

from hexawyn.application.ports.driven.stale_credentials_port import StaleCredentialRaw
from kubernetes import client, config


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut: MutantDict = {}  # type: ignore


class EmptyStaleCredentialsSource:
    @_mutmut_mutated(mutants_xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut)
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
    def xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut_orig(self, min_days: int) -> list[StaleCredentialRaw]:
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
    def xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut_1(self, min_days: int) -> list[StaleCredentialRaw]:
        try:
            config.load_kube_config()
            v1 = None
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
    def xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut_2(self, min_days: int) -> list[StaleCredentialRaw]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()
            secrets = None
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
    def xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut_3(self, min_days: int) -> list[StaleCredentialRaw]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()
            secrets = v1.list_secret_for_all_namespaces()
            cutoff = None

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
    def xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut_4(self, min_days: int) -> list[StaleCredentialRaw]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()
            secrets = v1.list_secret_for_all_namespaces()
            cutoff = datetime.datetime.now(datetime.UTC) + datetime.timedelta(days=min_days)

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
    def xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut_5(self, min_days: int) -> list[StaleCredentialRaw]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()
            secrets = v1.list_secret_for_all_namespaces()
            cutoff = datetime.datetime.now(None) - datetime.timedelta(days=min_days)

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
    def xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut_6(self, min_days: int) -> list[StaleCredentialRaw]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()
            secrets = v1.list_secret_for_all_namespaces()
            cutoff = datetime.datetime.now(datetime.UTC) - datetime.timedelta(days=None)

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
    def xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut_7(self, min_days: int) -> list[StaleCredentialRaw]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()
            secrets = v1.list_secret_for_all_namespaces()
            cutoff = datetime.datetime.now(datetime.UTC) - datetime.timedelta(days=min_days)

            result: list[StaleCredentialRaw] = None
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
    def xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut_8(self, min_days: int) -> list[StaleCredentialRaw]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()
            secrets = v1.list_secret_for_all_namespaces()
            cutoff = datetime.datetime.now(datetime.UTC) - datetime.timedelta(days=min_days)

            result: list[StaleCredentialRaw] = []
            for secret in secrets.items:
                if secret.metadata:
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
    def xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut_9(self, min_days: int) -> list[StaleCredentialRaw]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()
            secrets = v1.list_secret_for_all_namespaces()
            cutoff = datetime.datetime.now(datetime.UTC) - datetime.timedelta(days=min_days)

            result: list[StaleCredentialRaw] = []
            for secret in secrets.items:
                if not secret.metadata:
                    break
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
    def xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut_10(self, min_days: int) -> list[StaleCredentialRaw]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()
            secrets = v1.list_secret_for_all_namespaces()
            cutoff = datetime.datetime.now(datetime.UTC) - datetime.timedelta(days=min_days)

            result: list[StaleCredentialRaw] = []
            for secret in secrets.items:
                if not secret.metadata:
                    continue
                created = None
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
    def xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut_11(self, min_days: int) -> list[StaleCredentialRaw]:
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
                if created or created.replace(tzinfo=datetime.UTC) < cutoff:
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
    def xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut_12(self, min_days: int) -> list[StaleCredentialRaw]:
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
                if created and created.replace(tzinfo=None) < cutoff:
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
    def xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut_13(self, min_days: int) -> list[StaleCredentialRaw]:
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
                if created and created.replace(tzinfo=datetime.UTC) <= cutoff:
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
    def xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut_14(self, min_days: int) -> list[StaleCredentialRaw]:
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
                        None
                    )
            return result
        except Exception:
            return []
    def xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut_15(self, min_days: int) -> list[StaleCredentialRaw]:
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
                            name=None,
                            namespace=secret.metadata.namespace or "",
                            age_days=min_days,
                            type=secret.type or "Opaque",
                        )
                    )
            return result
        except Exception:
            return []
    def xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut_16(self, min_days: int) -> list[StaleCredentialRaw]:
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
                            namespace=None,
                            age_days=min_days,
                            type=secret.type or "Opaque",
                        )
                    )
            return result
        except Exception:
            return []
    def xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut_17(self, min_days: int) -> list[StaleCredentialRaw]:
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
                            age_days=None,
                            type=secret.type or "Opaque",
                        )
                    )
            return result
        except Exception:
            return []
    def xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut_18(self, min_days: int) -> list[StaleCredentialRaw]:
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
                            type=None,
                        )
                    )
            return result
        except Exception:
            return []
    def xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut_19(self, min_days: int) -> list[StaleCredentialRaw]:
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
                            namespace=secret.metadata.namespace or "",
                            age_days=min_days,
                            type=secret.type or "Opaque",
                        )
                    )
            return result
        except Exception:
            return []
    def xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut_20(self, min_days: int) -> list[StaleCredentialRaw]:
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
                            age_days=min_days,
                            type=secret.type or "Opaque",
                        )
                    )
            return result
        except Exception:
            return []
    def xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut_21(self, min_days: int) -> list[StaleCredentialRaw]:
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
                            type=secret.type or "Opaque",
                        )
                    )
            return result
        except Exception:
            return []
    def xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut_22(self, min_days: int) -> list[StaleCredentialRaw]:
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
                            )
                    )
            return result
        except Exception:
            return []
    def xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut_23(self, min_days: int) -> list[StaleCredentialRaw]:
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
                            name=secret.metadata.name and "",
                            namespace=secret.metadata.namespace or "",
                            age_days=min_days,
                            type=secret.type or "Opaque",
                        )
                    )
            return result
        except Exception:
            return []
    def xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut_24(self, min_days: int) -> list[StaleCredentialRaw]:
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
                            name=secret.metadata.name or "XXXX",
                            namespace=secret.metadata.namespace or "",
                            age_days=min_days,
                            type=secret.type or "Opaque",
                        )
                    )
            return result
        except Exception:
            return []
    def xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut_25(self, min_days: int) -> list[StaleCredentialRaw]:
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
                            namespace=secret.metadata.namespace and "",
                            age_days=min_days,
                            type=secret.type or "Opaque",
                        )
                    )
            return result
        except Exception:
            return []
    def xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut_26(self, min_days: int) -> list[StaleCredentialRaw]:
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
                            namespace=secret.metadata.namespace or "XXXX",
                            age_days=min_days,
                            type=secret.type or "Opaque",
                        )
                    )
            return result
        except Exception:
            return []
    def xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut_27(self, min_days: int) -> list[StaleCredentialRaw]:
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
                            type=secret.type and "Opaque",
                        )
                    )
            return result
        except Exception:
            return []
    def xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut_28(self, min_days: int) -> list[StaleCredentialRaw]:
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
                            type=secret.type or "XXOpaqueXX",
                        )
                    )
            return result
        except Exception:
            return []
    def xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut_29(self, min_days: int) -> list[StaleCredentialRaw]:
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
                            type=secret.type or "opaque",
                        )
                    )
            return result
        except Exception:
            return []
    def xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut_30(self, min_days: int) -> list[StaleCredentialRaw]:
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
                            type=secret.type or "OPAQUE",
                        )
                    )
            return result
        except Exception:
            return []

mutants_xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut['_mutmut_orig'] = EmptyStaleCredentialsSource.xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut_orig # type: ignore # mutmut generated
mutants_xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut['xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut_1'] = EmptyStaleCredentialsSource.xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut_1 # type: ignore # mutmut generated
mutants_xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut['xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut_2'] = EmptyStaleCredentialsSource.xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut_2 # type: ignore # mutmut generated
mutants_xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut['xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut_3'] = EmptyStaleCredentialsSource.xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut_3 # type: ignore # mutmut generated
mutants_xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut['xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut_4'] = EmptyStaleCredentialsSource.xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut_4 # type: ignore # mutmut generated
mutants_xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut['xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut_5'] = EmptyStaleCredentialsSource.xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut_5 # type: ignore # mutmut generated
mutants_xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut['xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut_6'] = EmptyStaleCredentialsSource.xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut_6 # type: ignore # mutmut generated
mutants_xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut['xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut_7'] = EmptyStaleCredentialsSource.xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut_7 # type: ignore # mutmut generated
mutants_xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut['xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut_8'] = EmptyStaleCredentialsSource.xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut_8 # type: ignore # mutmut generated
mutants_xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut['xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut_9'] = EmptyStaleCredentialsSource.xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut_9 # type: ignore # mutmut generated
mutants_xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut['xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut_10'] = EmptyStaleCredentialsSource.xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut_10 # type: ignore # mutmut generated
mutants_xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut['xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut_11'] = EmptyStaleCredentialsSource.xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut_11 # type: ignore # mutmut generated
mutants_xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut['xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut_12'] = EmptyStaleCredentialsSource.xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut_12 # type: ignore # mutmut generated
mutants_xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut['xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut_13'] = EmptyStaleCredentialsSource.xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut_13 # type: ignore # mutmut generated
mutants_xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut['xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut_14'] = EmptyStaleCredentialsSource.xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut_14 # type: ignore # mutmut generated
mutants_xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut['xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut_15'] = EmptyStaleCredentialsSource.xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut_15 # type: ignore # mutmut generated
mutants_xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut['xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut_16'] = EmptyStaleCredentialsSource.xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut_16 # type: ignore # mutmut generated
mutants_xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut['xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut_17'] = EmptyStaleCredentialsSource.xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut_17 # type: ignore # mutmut generated
mutants_xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut['xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut_18'] = EmptyStaleCredentialsSource.xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut_18 # type: ignore # mutmut generated
mutants_xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut['xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut_19'] = EmptyStaleCredentialsSource.xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut_19 # type: ignore # mutmut generated
mutants_xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut['xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut_20'] = EmptyStaleCredentialsSource.xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut_20 # type: ignore # mutmut generated
mutants_xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut['xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut_21'] = EmptyStaleCredentialsSource.xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut_21 # type: ignore # mutmut generated
mutants_xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut['xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut_22'] = EmptyStaleCredentialsSource.xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut_22 # type: ignore # mutmut generated
mutants_xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut['xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut_23'] = EmptyStaleCredentialsSource.xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut_23 # type: ignore # mutmut generated
mutants_xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut['xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut_24'] = EmptyStaleCredentialsSource.xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut_24 # type: ignore # mutmut generated
mutants_xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut['xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut_25'] = EmptyStaleCredentialsSource.xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut_25 # type: ignore # mutmut generated
mutants_xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut['xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut_26'] = EmptyStaleCredentialsSource.xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut_26 # type: ignore # mutmut generated
mutants_xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut['xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut_27'] = EmptyStaleCredentialsSource.xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut_27 # type: ignore # mutmut generated
mutants_xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut['xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut_28'] = EmptyStaleCredentialsSource.xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut_28 # type: ignore # mutmut generated
mutants_xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut['xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut_29'] = EmptyStaleCredentialsSource.xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut_29 # type: ignore # mutmut generated
mutants_xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut['xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut_30'] = EmptyStaleCredentialsSource.xǁEmptyStaleCredentialsSourceǁfetch_stale_credentials__mutmut_30 # type: ignore # mutmut generated
