ZOMBIE_PODS_SCENARIO = {
    "context": {"name": "prod-eu", "cluster": "prod-eu", "provider": "vanilla"},
    "health": {"score": 85, "status": "healthy"},
    "pods": [
        {
            "name": "old-report-gen",
            "status": "Running",
            "restarts": 0,
            "namespace": "reporting",
            "cpu_request_millicores": 2000,
            "memory_request_mib": 4096,
        },
        {
            "name": "deprecated-batch",
            "status": "Running",
            "restarts": 0,
            "namespace": "batch",
            "cpu_request_millicores": 1000,
            "memory_request_mib": 2048,
        },
        {
            "name": "legacy-etl-1",
            "status": "Running",
            "restarts": 0,
            "namespace": "data",
            "cpu_request_millicores": 4000,
            "memory_request_mib": 8192,
        },
        {
            "name": "active-api-1",
            "status": "Running",
            "restarts": 0,
            "namespace": "production",
            "cpu_request_millicores": 2000,
            "memory_request_mib": 4096,
        },
        {
            "name": "cache-warmer-1",
            "status": "Running",
            "restarts": 0,
            "namespace": "cache",
            "cpu_request_millicores": 500,
            "memory_request_mib": 1024,
        },
    ],
    "metrics": {"cpu_usage_pct": 18, "memory_usage_pct": 22, "node_count": 8, "pod_count": 30},
    "findings": [
        {
            "severity": "medium",
            "message": "3 pods with 0 traffic for > 24h: old-report-gen, deprecated-batch, legacy-etl-1",  # noqa: E501
            "remediation": "Safe to decommission — saved $412/month",
        },
        {
            "severity": "medium",
            "message": "cache-warmer running idle at 0.1 RPS — consider scaling to 0 with KEDA",
            "remediation": "Estimated $47/month savings with scale-to-zero",
        },
        {
            "severity": "low",
            "message": "Total potential savings: $459/month from zombie cleanup",
            "remediation": "Decommission old-report-gen, deprecated-batch, legacy-etl-1 immediately",  # noqa: E501
        },
    ],
    "chips": ["Zombie pods", "Idle workloads", "Cost savings", "Safe to delete"],
    "slack_message": "🧟 Zombie pods detected: 3 idle workloads, $459/month potential savings.",
}
