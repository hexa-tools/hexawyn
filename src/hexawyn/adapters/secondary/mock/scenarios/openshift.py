OPENSHIFT_SCENARIO = {
    "context": {"name": "prod-ocp-east", "cluster": "openshift-prod", "provider": "openshift"},
    "health": {"score": 71, "status": "degraded"},
    "pods": [
        {"name": "catalog-api-2f8d1a-mk3x", "status": "Running", "restarts": 2, "namespace": "catalog"},
        {"name": "orders-worker-5c9b3e-qp7l", "status": "Running", "restarts": 0, "namespace": "orders"},
    ],
    "metrics": {"cpu_usage_pct": 61.8, "memory_usage_pct": 77.3, "node_count": 6, "pod_count": 24},
    "findings": [
        {
            "severity": "high",
            "message": "TLS certificate expiring in 7 days for admin-route",
            "remediation": "Renew TLS certificate via cert-manager",
        },
        {
            "severity": "medium",
            "message": "Pipeline build-app failed on last run",
            "remediation": "Check build logs and retry pipeline",
        },
    ],
    "chips": ["TLS cert expiring", "Failed pipeline", "Memory 77%"],
    "slack_message": "Alert: OpenShift — TLS cert expiring in 7 days, pipeline failed. Score 71.",
    "projects": ["production", "staging", "monitoring"],
    "routes": [
        {"name": "admin-route", "tls": False},
        {"name": "catalog-api-route", "tls": True},
    ],
    "pipeline_runs": [
        {"name": "build-app", "status": "Failed"},
        {"name": "deploy-staging", "status": "Succeeded"},
    ],
}
