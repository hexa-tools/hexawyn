AWS_EKS_SCENARIO = {
    "context": {"name": "prod-eks-us-east-1", "cluster": "eks-prod", "provider": "aws"},
    "health": {"score": 76, "status": "degraded"},
    "pods": [
        {
            "name": "payments-api-7d9f8b-m3ql",
            "status": "CrashLoop",
            "restarts": 8,
            "namespace": "payments",
        },
        {"name": "ml-worker-8b3a1e-hn7k", "status": "Pending", "restarts": 0, "namespace": "ml"},
        {"name": "auth-svc-4c2d9f-xp5j", "status": "Running", "restarts": 1, "namespace": "auth"},
    ],
    "metrics": {"cpu_usage_pct": 84.5, "memory_usage_pct": 72.1, "node_count": 12, "pod_count": 47},
    "findings": [
        {
            "severity": "critical",
            "message": "OOM kill detected in payments-api — memory limit 256Mi too low for peak load",
            "remediation": "Increase memory limit to 512Mi and enable HPA",
        },
        {
            "severity": "high",
            "message": "ml-worker stuck in Pending — insufficient GPU nodes",
            "remediation": "Add GPU node group or scale existing one",
        },
    ],
    "chips": ["CrashLoop in payments-api", "Pending ML worker", "OOM kill detected"],
    "slack_message": "Alert: EKS prod — OOM kill in payments-api. Score 76. Action: increase memory limit.",
}
