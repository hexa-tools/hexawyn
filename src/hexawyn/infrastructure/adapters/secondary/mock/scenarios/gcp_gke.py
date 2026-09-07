GCP_GKE_SCENARIO = {
    "context": {"name": "prod-gke-us-central1", "cluster": "gke-prod", "provider": "gcp"},
    "health": {"score": 84, "status": "degraded"},
    "pods": [
        {
            "name": "payments-api-3f7a2b-qw9k",
            "status": "Running",
            "restarts": 3,
            "namespace": "payments",
        },
        {
            "name": "inventory-svc-8b4c1d-zm5l",
            "status": "Running",
            "restarts": 0,
            "namespace": "inventory",
        },
    ],
    "metrics": {
        "cpu_usage_pct": 68.3,
        "memory_usage_pct": 91.5,
        "p99_latency_ms": 820,
        "slo_threshold_ms": 500,
        "node_count": 10,
        "pod_count": 38,
    },
    "findings": [
        {
            "severity": "critical",
            "message": "OOM prediction for payments-api — memory trending at 94% over 15min",
            "remediation": "Increase memory request to 1Gi and add HPA",
        },
        {
            "severity": "high",
            "message": "p99 latency 820ms exceeds SLO 500ms for payments-api",
            "remediation": "Investigate DB query performance and connection pooling",
        },
    ],
    "chips": ["SLO breach p99 820ms", "OOM risk payments-api", "Memory 91%"],
    "slack_message": "Alert: GKE prod — SLO breach payments-api p99=820ms (target 500ms). Score 84.",  # noqa: E501
}
