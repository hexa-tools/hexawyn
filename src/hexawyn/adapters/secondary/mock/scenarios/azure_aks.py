AZURE_AKS_SCENARIO = {
    "context": {"name": "prod-aks-westeurope", "cluster": "aks-prod", "provider": "azure"},
    "health": {"score": 98, "status": "healthy"},
    "pods": [
        {"name": "frontend-7b4c8d-mn3k", "status": "Running", "restarts": 0, "namespace": "web"},
        {"name": "api-gateway-2d9f1a-xp5j", "status": "Running", "restarts": 0, "namespace": "api"},
        {
            "name": "redis-cache-5a3b7e-kl2m",
            "status": "Running",
            "restarts": 0,
            "namespace": "cache",
        },
    ],
    "metrics": {"cpu_usage_pct": 34.2, "memory_usage_pct": 41.8, "node_count": 8, "pod_count": 32},
    "findings": [
        {
            "severity": "low",
            "message": "AKS cluster healthy — no action required",
            "remediation": "Continue monitoring node pool auto-scaling",
        },
    ],
    "chips": ["All pods healthy", "CPU usage 34%", "No critical findings"],
    "slack_message": "Info: AKS prod — all systems healthy. Score 98. No action needed.",
}
