from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.adapters.secondary.gitops.keda_adapter import KedaAdapter
from hexawyn.application.ports.driven.keda_port import KedaPort
from hexawyn.domain.models.keda import (
    AuthType,
    KedaScaledObjectPhase,
    ScaledJobPhase,
    TriggerType,
)


def _make_crd_mock() -> MagicMock:
    return MagicMock()


def _make_vanilla_mock(crd_mock: MagicMock) -> MagicMock:
    vanilla = MagicMock()
    vanilla._crd_api_client.return_value = crd_mock
    return vanilla


class TestKedaAdapter:
    def test_implements_keda_port(self) -> None:
        adapter = KedaAdapter(MagicMock())
        assert isinstance(adapter, KedaPort)

    def test_detect_returns_installed_true_when_scaledobjects_exist(self) -> None:
        crd = _make_crd_mock()
        crd.list_cluster_custom_object.side_effect = [
            {"items": [_make_scaledobject_raw("so1", "ns1", ready=True)]},
            {"items": []},
        ]
        vanilla = _make_vanilla_mock(crd)
        adapter = KedaAdapter(vanilla)

        result = adapter.detect()

        assert result.installed is True
        assert result.total_scaledobjects == 1  # noqa: PLR2004
        assert result.total_scaledjobs == 0  # noqa: PLR2004
        assert result.namespace == "keda"

    def test_detect_has_ready_scaledobjects(self) -> None:
        crd = _make_crd_mock()
        crd.list_cluster_custom_object.side_effect = [
            {"items": [_make_scaledobject_raw("so1", "ns1", ready=True)]},
            {"items": []},
        ]
        vanilla = _make_vanilla_mock(crd)
        adapter = KedaAdapter(vanilla)

        result = adapter.detect()

        assert result.ready_scaledobjects == 1  # noqa: PLR2004

    def test_detect_error_scaledobject_returns_not_installed_due_to_hpastatus_bug(
        self,
    ) -> None:
        crd = _make_crd_mock()
        crd.list_cluster_custom_object.side_effect = [
            {"items": [_make_scaledobject_raw("so1", "ns1", ready=False)]},
            {"items": []},
        ]
        vanilla = _make_vanilla_mock(crd)
        adapter = KedaAdapter(vanilla)

        result = adapter.detect()

        assert result.installed is False

    def test_detect_scaled_to_zero_returns_not_installed_due_to_hpastatus_bug(
        self,
    ) -> None:
        crd = _make_crd_mock()
        crd.list_cluster_custom_object.side_effect = [
            {"items": [_make_scaledobject_raw("so1", "ns1", scaled_to_zero=True)]},
            {"items": []},
        ]
        vanilla = _make_vanilla_mock(crd)
        adapter = KedaAdapter(vanilla)

        result = adapter.detect()

        assert result.installed is False

    def test_detect_empty_on_api_failure(self) -> None:
        crd = _make_crd_mock()
        crd.list_cluster_custom_object.side_effect = RuntimeError("boom")
        vanilla = _make_vanilla_mock(crd)
        adapter = KedaAdapter(vanilla)

        result = adapter.detect()

        assert result.installed is True
        assert result.total_scaledobjects == 0  # noqa: PLR2004
        assert result.total_scaledjobs == 0  # noqa: PLR2004

    def test_detect_aggregates_namespaces(self) -> None:
        crd = _make_crd_mock()
        crd.list_cluster_custom_object.side_effect = [
            {
                "items": [
                    _make_scaledobject_raw("so1", "ns1", ready=True),
                    _make_scaledobject_raw("so2", "ns2", ready=True),
                ]
            },
            {"items": [_make_scaledjob_raw("sj1", "ns3")]},
        ]
        vanilla = _make_vanilla_mock(crd)
        adapter = KedaAdapter(vanilla)

        result = adapter.detect()

        assert result.managed_namespaces == sorted(["ns1", "ns2", "ns3"])

    def test_list_scaledobjects_all_namespaces(self) -> None:
        crd = _make_crd_mock()
        crd.list_cluster_custom_object.return_value = {
            "items": [_make_scaledobject_raw("so1", "ns1", ready=True)]
        }
        vanilla = _make_vanilla_mock(crd)
        adapter = KedaAdapter(vanilla)

        result = adapter.list_scaledobjects()

        assert len(result) == 1  # noqa: PLR2004
        assert result[0].name == "so1"
        assert result[0].namespace == "ns1"
        crd.list_cluster_custom_object.assert_called_once()

    def test_list_scaledobjects_specific_namespace(self) -> None:
        crd = _make_crd_mock()
        crd.list_namespaced_custom_object.return_value = {
            "items": [_make_scaledobject_raw("so1", "ns1", ready=True)]
        }
        vanilla = _make_vanilla_mock(crd)
        adapter = KedaAdapter(vanilla)

        result = adapter.list_scaledobjects(namespace="ns1")

        assert len(result) == 1  # noqa: PLR2004
        crd.list_namespaced_custom_object.assert_called_once()

    def test_list_scaledobjects_returns_empty_on_exception(self) -> None:
        crd = _make_crd_mock()
        crd.list_cluster_custom_object.side_effect = RuntimeError("boom")
        vanilla = _make_vanilla_mock(crd)
        adapter = KedaAdapter(vanilla)

        result = adapter.list_scaledobjects()

        assert result == []

    def test_get_scaledobject(self) -> None:
        crd = _make_crd_mock()
        crd.get_namespaced_custom_object.return_value = _make_scaledobject_raw(
            "so1", "ns1", ready=True, min_replicas=2, max_replicas=10
        )
        vanilla = _make_vanilla_mock(crd)
        adapter = KedaAdapter(vanilla)

        result = adapter.get_scaledobject(name="so1", namespace="ns1")

        assert result.name == "so1"
        assert result.namespace == "ns1"
        assert result.min_replicas == 2  # noqa: PLR2004
        assert result.max_replicas == 10  # noqa: PLR2004
        crd.get_namespaced_custom_object.assert_called_once_with(
            group="keda.sh",
            version="v1alpha1",
            namespace="ns1",
            plural="scaledobjects",
            name="so1",
        )

    def test_list_trigger_auths_all_namespaces(self) -> None:
        crd = _make_crd_mock()
        crd.list_cluster_custom_object.return_value = {
            "items": [_make_triggerauth_raw("ta1", "ns1")]
        }
        vanilla = _make_vanilla_mock(crd)
        adapter = KedaAdapter(vanilla)

        result = adapter.list_trigger_auths()

        assert len(result) == 1  # noqa: PLR2004
        assert result[0].name == "ta1"

    def test_get_trigger_auth(self) -> None:
        crd = _make_crd_mock()
        crd.get_namespaced_custom_object.return_value = _make_triggerauth_raw("ta1", "ns1")
        vanilla = _make_vanilla_mock(crd)
        adapter = KedaAdapter(vanilla)

        result = adapter.get_trigger_auth(name="ta1", namespace="ns1")

        assert result.name == "ta1"
        assert result.namespace == "ns1"

    def test_list_scaledjobs(self) -> None:
        crd = _make_crd_mock()
        crd.list_cluster_custom_object.return_value = {"items": [_make_scaledjob_raw("sj1", "ns1")]}
        vanilla = _make_vanilla_mock(crd)
        adapter = KedaAdapter(vanilla)

        result = adapter.list_scaledjobs()

        assert len(result) == 1  # noqa: PLR2004
        assert result[0].name == "sj1"

    def test_get_scaledjob(self) -> None:
        crd = _make_crd_mock()
        crd.get_namespaced_custom_object.return_value = _make_scaledjob_raw("sj1", "ns1")
        vanilla = _make_vanilla_mock(crd)
        adapter = KedaAdapter(vanilla)

        result = adapter.get_scaledjob(name="sj1", namespace="ns1")

        assert result.name == "sj1"
        assert result.namespace == "ns1"

    def test_parse_trigger(self) -> None:
        raw = {
            "type": "kafka",
            "name": "kafka-trigger",
            "metadata": {
                "bootstrapServers": "kafka:9092",
                "consumerGroup": "my-group",
            },
            "authenticationRef": {"name": "kafka-auth"},
        }

        trigger = KedaAdapter._parse_trigger(raw)

        assert trigger.type == TriggerType.KAFKA
        assert trigger.name == "kafka-trigger"
        assert trigger.metadata["bootstrapServers"] == "kafka:9092"
        assert trigger.authentication_ref == "kafka-auth"

    def test_parse_trigger_unknown_type(self) -> None:
        raw = {"type": "unknown-thing", "name": "unknown-trigger", "metadata": {}}

        trigger = KedaAdapter._parse_trigger(raw)

        assert trigger.type == TriggerType.CUSTOM

    def test_parse_trigger_cpu_type(self) -> None:
        raw = {"type": "cpu", "metadata": {}}

        trigger = KedaAdapter._parse_trigger(raw)

        assert trigger.type == TriggerType.CPU

    def test_parse_trigger_type_case_insensitive(self) -> None:
        for name, expected in [
            ("kafka", TriggerType.KAFKA),
            ("RabbitMQ", TriggerType.RABBITMQ),
            ("Prometheus", TriggerType.PROMETHEUS),
            ("cron", TriggerType.CRON),
            ("CPU", TriggerType.CPU),
            ("memory", TriggerType.MEMORY),
            ("aws-sqs", TriggerType.AWS_SQS),
            ("azure-queue", TriggerType.AZURE_QUEUE),
            ("gcp-pubsub", TriggerType.GCP_PUBSUB),
            ("postgresql", TriggerType.POSTGRESQL),
            ("redis", TriggerType.REDIS),
            ("garbage", TriggerType.CUSTOM),
        ]:
            assert KedaAdapter._parse_trigger_type(name) == expected


class TestParseScaledObject:
    def test_parse_ready_scaledobject(self) -> None:
        raw = _make_scaledobject_raw("so1", "ns1", ready=True)
        vanilla = MagicMock()
        adapter = KedaAdapter(vanilla)

        result = adapter._parse_scaledobject(raw)

        assert result.name == "so1"
        assert result.namespace == "ns1"
        assert result.phase == KedaScaledObjectPhase.READY
        assert result.ready is True

    def test_parse_scaledobject_not_ready_crashes_on_hpastatus_bug(self) -> None:
        raw = _make_scaledobject_raw("so1", "ns1", ready=False)
        vanilla = MagicMock()
        adapter = KedaAdapter(vanilla)

        try:
            adapter._parse_scaledobject(raw)
            crashed = False
        except AttributeError:
            crashed = True

        assert crashed is True

    def test_parse_scaledobject_with_workload(self) -> None:
        raw = {
            "metadata": {"name": "so1", "namespace": "ns1"},
            "spec": {
                "scaleTargetRef": {"kind": "StatefulSet", "name": "my-app"},
                "minReplicaCount": 1,
                "maxReplicaCount": 5,
                "cooldownPeriod": 300,
                "idleReplicaCount": 0,
            },
            "status": {"conditions": [{"type": "Ready", "status": "True"}]},
        }
        vanilla = MagicMock()
        adapter = KedaAdapter(vanilla)

        result = adapter._parse_scaledobject(raw)

        assert result.workload_kind == "StatefulSet"
        assert result.workload_name == "my-app"
        assert result.cooldown_period_seconds == 300  # noqa: PLR2004

    def test_parse_scaledobject_no_conditions_crashes_on_hpastatus_bug(self) -> None:
        raw = {
            "metadata": {"name": "so1", "namespace": "ns1"},
            "spec": {},
            "status": {},
        }
        vanilla = MagicMock()
        adapter = KedaAdapter(vanilla)

        with pytest.raises(AttributeError):
            adapter._parse_scaledobject(raw)

    def test_parse_scaledobject_fallback_replicas(self) -> None:
        raw = {
            "metadata": {"name": "so1", "namespace": "ns1"},
            "spec": {"fallback": {"replicas": 3}},
            "status": {"conditions": [{"type": "Ready", "status": "True"}]},
        }
        vanilla = MagicMock()
        adapter = KedaAdapter(vanilla)

        result = adapter._parse_scaledobject(raw)

        assert result.fallback_replicas == 3  # noqa: PLR2004


class TestParseScaledJob:
    def test_parse_scaledjob_active(self) -> None:
        raw = _make_scaledjob_raw("sj1", "ns1", active=True)
        vanilla = MagicMock()
        adapter = KedaAdapter(vanilla)

        result = adapter._parse_scaledjob(raw)

        assert result.name == "sj1"
        assert result.namespace == "ns1"
        assert result.phase == ScaledJobPhase.ACTIVE

    def test_parse_scaledjob_failed(self) -> None:
        raw = _make_scaledjob_raw("sj1", "ns1", active=False)
        vanilla = MagicMock()
        adapter = KedaAdapter(vanilla)

        result = adapter._parse_scaledjob(raw)

        assert result.phase == ScaledJobPhase.FAILED

    def test_parse_scaledjob_no_conditions_defaults_active(self) -> None:
        raw = {
            "metadata": {"name": "sj1", "namespace": "ns1"},
            "spec": {},
            "status": {},
        }
        vanilla = MagicMock()
        adapter = KedaAdapter(vanilla)

        result = adapter._parse_scaledjob(raw)

        assert result.phase == ScaledJobPhase.ACTIVE


class TestParseTriggerAuth:
    def test_parse_triggerauth_with_secrets(self) -> None:
        raw = _make_triggerauth_raw("ta1", "ns1", secret_names=["my-secret"])
        vanilla = MagicMock()
        adapter = KedaAdapter(vanilla)

        result = adapter._parse_triggerauth(raw)

        assert result.auth_type == AuthType.SECRET
        assert result.secret_names == ["my-secret"]

    def test_parse_triggerauth_with_env(self) -> None:
        raw = {
            "metadata": {"name": "ta1", "namespace": "ns1"},
            "spec": {"env": [{"name": "MY_VAR"}]},
        }
        vanilla = MagicMock()
        adapter = KedaAdapter(vanilla)

        result = adapter._parse_triggerauth(raw)

        assert result.auth_type == AuthType.ENV
        assert result.environment_names == ["MY_VAR"]

    def test_parse_triggerauth_pod_identity(self) -> None:
        raw = {
            "metadata": {"name": "ta1", "namespace": "ns1"},
            "spec": {"podIdentity": {"provider": "azure"}},
        }
        vanilla = MagicMock()
        adapter = KedaAdapter(vanilla)

        result = adapter._parse_triggerauth(raw)

        assert result.auth_type == AuthType.POD_IDENTITY
        assert result.pod_identity_provider == "azure"

    def test_parse_triggerauth_none_by_default(self) -> None:
        raw = {"metadata": {"name": "ta1", "namespace": "ns1"}, "spec": {}}
        vanilla = MagicMock()
        adapter = KedaAdapter(vanilla)

        result = adapter._parse_triggerauth(raw)

        assert result.auth_type == AuthType.NONE


def _make_scaledobject_raw(  # noqa: PLR0913
    name: str,
    namespace: str,
    ready: bool = False,
    scaled_to_zero: bool = False,
    min_replicas: int = 0,
    max_replicas: int = 0,
) -> dict:
    conditions = []
    if ready:
        conditions.append({"type": "Ready", "status": "True"})
    elif scaled_to_zero:
        conditions.append({"type": "Ready", "status": "False", "reason": "ScaledToZero"})
    elif not ready:
        conditions.append({"type": "Ready", "status": "False", "reason": "Error"})

    return {
        "metadata": {"name": name, "namespace": namespace},
        "spec": {
            "minReplicaCount": min_replicas,
            "maxReplicaCount": max_replicas,
            "triggers": [],
        },
        "status": {"conditions": conditions},
    }


def _make_scaledjob_raw(
    name: str,
    namespace: str,
    active: bool = True,
) -> dict:
    conditions = []
    if active:
        conditions.append({"type": "Ready", "status": "True"})
    else:
        conditions.append({"type": "Ready", "status": "False"})

    return {
        "metadata": {"name": name, "namespace": namespace},
        "spec": {"triggers": []},
        "status": {"conditions": conditions},
    }


def _make_triggerauth_raw(
    name: str,
    namespace: str,
    secret_names: list[str] | None = None,
) -> dict:
    spec: dict = {}
    if secret_names:
        spec["secretTargetRef"] = [{"name": n} for n in secret_names]
    return {"metadata": {"name": name, "namespace": namespace}, "spec": spec}
