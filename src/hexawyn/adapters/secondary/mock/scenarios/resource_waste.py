RESOURCE_WASTE_SCENARIO = {
    "context": {"name": "prod-eu", "cluster": "prod-eu", "provider": "vanilla"},
    "health": {"score": 78, "status": "healthy"},
    "pods": [
        {"name": "dev-legacy-1", "status": "Running", "restarts": 0, "namespace": "dev", "cpu_request_millicores": 8000, "memory_request_mib": 32768},
        {"name": "ml-trainer-1", "status": "Running", "restarts": 0, "namespace": "ml", "cpu_request_millicores": 16000, "memory_request_mib": 65536},
        {"name": "staging-api-1", "status": "Running", "restarts": 0, "namespace": "staging", "cpu_request_millicores": 4000, "memory_request_mib": 16384},
        {"name": "prod-api-1", "status": "Running", "restarts": 0, "namespace": "production", "cpu_request_millicores": 2000, "memory_request_mib": 8192},
        {"name": "qa-runner-1", "status": "Running", "restarts": 0, "namespace": "qa", "cpu_request_millicores": 6000, "memory_request_mib": 24576},
    ],
    "metrics": {"cpu_usage_pct": 23, "memory_usage_pct": 19, "node_count": 6, "pod_count": 22},
    "findings": [
        {"severity": "high", "message": "dev namespace requests 8 CPUs but uses < 2 — 600% over-provisioned", "remediation": "Right-size dev namespace to 2 CPUs"},
        {"severity": "high", "message": "ml namespace requests 16 CPUs but uses ~4 — 400% over-provisioned", "remediation": "Reduce ml workloads to 6 CPU requests"},
        {"severity": "medium", "message": "staging and qa combined waste ~8 CPUs and 40Gi", "remediation": "Apply namespace resource quotas"},
    ],
    "chips": ["Over-provisioned namespaces", "Right-sizing savings", "Team cost breakdown"],
    "slack_message": "💰 Savings alert: dev, ml, staging over-provisioned by 300-600%. Estimated monthly savings: $823.",
}
