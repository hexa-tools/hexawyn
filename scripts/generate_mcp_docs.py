"""Génère docs/MCP_TOOLS.md à partir des tools MCP exposés par hexawyn.

Usage : python scripts/generate_mcp_docs.py
À lancer en CI sur chaque merge vers main pour garder la doc à jour.
"""

from __future__ import annotations

from pathlib import Path

from hexawyn.domain.models.mcp_tool import MCPToolRegistry, MCPToolSchema

OUTPUT_PATH = Path("docs/MCP_TOOLS.md")

_CATEGORY_MAP: dict[str, str] = {
    "list_": "Core Operations",
    "get_": "Core Operations",
    "describe_": "Core Operations",
    "forecast_": "FinOps",
    "estimate_": "FinOps",
    "compute_team": "FinOps",
    "compare_service": "FinOps",
    "project_budget": "FinOps",
    "cost_profiling": "FinOps",
    "rightsizing": "FinOps",
    "over_provisioned": "FinOps",
    "audit_": "Security",
    "detect_privileged": "Security",
    "report_": "Security",
    "scan_": "Security",
    "sensitive_": "Security",
    "rbac_": "Security",
    "security": "Security",
    "admin_endpoint": "Security",
    "gitops_": "GitOps",
    "certs_": "Certificates",
    "pipeline": "Pipelines",
    "task_run": "Pipelines",
    "analyze_failed": "Pipelines",
    "policy_": "Policy",
    "rollouts_": "Rollouts",
    "canary_": "Rollouts",
    "keda_": "KEDA Autoscaling",
    "reliability": "Reliability",
    "mttr": "Reliability",
    "mttd": "Reliability",
    "incident": "Reliability",
    "slo_": "Reliability",
    "error_budget": "Reliability",
    "detect_recurring": "Reliability",
    "logs": "Logs",
    "log_": "Logs",
    "drift": "Drift / Config",
    "diff_": "Drift / Config",
    "capacity": "Capacity",
    "headroom": "Capacity",
    "spike_": "Capacity",
    "network_": "Network",
    "route_": "Network",
    "ingress": "Network",
    "helm": "Helm",
    "prometheus": "Observability",
    "p99_": "Observability",
    "latency": "Observability",
    "memory": "Observability",
    "saturation": "Observability",
    "bottleneck": "Observability",
    "hot_node": "Observability",
    "diagnose_": "Observability",
    "span_": "Observability",
    "deployment_latency": "Observability",
    "global_health": "Observability",
    "detect_zombies": "FinOps",
    "detect_outdated": "FinOps",
    "detect_pod_anomalies": "Observability",
    "detect_": "Observability",
    "custom_tool": "Custom Tools",
    "compare_cluster": "Core Operations",
    "generate_": "Reliability",
    "watch_": "Logs",
    "semantic": "Logs",
    "etcd_": "Core Operations",
    "cloud": "Core Operations",
}


def _categorize(name: str) -> str:
    for prefix, category in sorted(_CATEGORY_MAP.items(), key=lambda x: -len(x[0])):
        if name.startswith(prefix) or prefix in name:
            return category
    return "Other"


def _group_by_category(tools: list[MCPToolSchema]) -> dict[str, list[MCPToolSchema]]:
    groups: dict[str, list[MCPToolSchema]] = {}
    for tool in tools:
        cat = _categorize(tool.name)
        groups.setdefault(cat, []).append(tool)
    return groups


def _build_example(tool: MCPToolSchema) -> str:
    props = tool.input_schema.get("properties", {})
    args: dict[str, object] = {}
    for name, schema in props.items():
        schema = schema if isinstance(schema, dict) else {}
        t = schema.get("type", "string")
        if t == "string":
            args[name] = schema.get("default", "example") if "default" in schema else "example"
        elif t == "integer":
            args[name] = schema.get("default", 42) if "default" in schema else 42
        elif t == "number":
            args[name] = schema.get("default", 1.0) if "default" in schema else 1.0
        elif t == "boolean":
            args[name] = schema.get("default", False) if "default" in schema else False
        elif t == "array":
            args[name] = []
        else:
            args[name] = "..."
    import json

    return json.dumps({"tool": tool.name, "arguments": args}, indent=2)


def generate_markdown(registry: MCPToolRegistry) -> str:
    lines = [
        "# hexawyn — MCP Tools Reference",
        "",
        f"Auto-generated from `tools/list`. {len(registry.tools)} tools available.",
        "",
        "> ⚠️ This file is auto-generated — do not edit manually.",
        "> Run `python scripts/generate_mcp_docs.py` to regenerate.",
        "",
        "---",
        "",
    ]

    groups = _group_by_category(registry.tools)

    order: list[str] = [
        "Core Operations",
        "Observability",
        "FinOps",
        "Security",
        "Reliability",
        "Capacity",
        "Network",
        "Logs",
        "GitOps",
        "Helm",
        "Certificates",
        "Pipelines",
        "Policy",
        "Rollouts",
        "KEDA Autoscaling",
        "Drift / Config",
        "Custom Tools",
        "Other",
    ]

    for category in order:
        tools = groups.pop(category, [])
        if not tools:
            continue
        tools.sort(key=lambda t: t.name)
        lines.append(f"## {category}")
        lines.append("")
        for tool in tools:
            lines.append(f"### `{tool.name}`")
            lines.append("")
            lines.append(tool.description)
            lines.append("")
            lines.append("**Parameters:**")
            lines.append("")
            props = tool.input_schema.get("properties", {})
            if not props:
                lines.append("No parameters.")
                lines.append("")
            else:
                required_list: list[str] = list(tool.input_schema.get("required", []))
                lines.append("| Name | Type | Required | Description |")
                lines.append("|------|------|----------|-------------|")
                for param_name, param_schema in props.items():
                    param_schema = param_schema if isinstance(param_schema, dict) else {}
                    required = "✅" if param_name in required_list else "❌"
                    desc = param_schema.get("description", "—")
                    ptype = param_schema.get("type", "any")
                    lines.append(
                        f"| `{param_name}` | `{ptype}` | {required} | {desc} |"
                    )
                lines.append("")
            lines.append("**Example:**")
            lines.append("```json")
            lines.append(_build_example(tool))
            lines.append("```")
            lines.append("")
            lines.append("---")
            lines.append("")

    for category, tools in sorted(groups.items()):
        tools.sort(key=lambda t: t.name)
        lines.append(f"## {category}")
        lines.append("")
        for tool in tools:
            lines.append(f"### `{tool.name}`")
            lines.append("")
            lines.append(tool.description)
            lines.append("")
            lines.append("---")
            lines.append("")

    return "\n".join(lines)


def main() -> None:
    from hexawyn.adapters.secondary.mcp.mcp_discovery_adapter import MCPDiscoveryAdapter

    discovery = MCPDiscoveryAdapter()
    registry = discovery.discover()
    markdown = generate_markdown(registry)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(markdown)
    print(f"Generated {OUTPUT_PATH} with {len(registry.tools)} tools")


if __name__ == "__main__":
    main()
