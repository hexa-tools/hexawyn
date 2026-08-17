from typing import Any

from hexawyn.cli.presentation.asides import (
    failed_pod_count,
    kubectl_current_context,
    mapping_int,
    namespace_count,
    pending_pod_count,
    running_pod_count,
    safe_findings,
    safe_health_score,
    safe_metrics,
    safe_pods,
    safe_suggestions,
)
from hexawyn.cli.presentation.findings import format_finding_warnings
from hexawyn.cli.presentation.formatting import connection_line
from hexawyn.cli.presentation.license_display import format_license_aside_lines
from hexawyn.cli.presentation.suggestions import format_suggestion_lines


def build_aside_lines(app: Any) -> list[str]:
    ctx = app.adapter.get_cluster_context()
    pods = safe_pods(app.adapter)
    metrics = safe_metrics(app.adapter)
    findings = safe_findings(app.adapter)
    suggestions = safe_suggestions(app.adapter)

    cluster_name = str(ctx.get("name", "unknown"))
    namespace = str(ctx.get("namespace", "default"))
    pod_count = mapping_int(metrics, "pod_count", len(pods))
    node_count = mapping_int(metrics, "node_count", 0)
    kubectl_ctx = kubectl_current_context()

    lines = [
        "[bold]HEXAWYN[/bold]",
        "",
        connection_line(app.startup_status),
        "",
        f"Cluster: [bold]{cluster_name}[/bold]",
        f"Context: [dim]{kubectl_ctx}[/dim]",
        f"Namespace: [bold]{namespace}[/bold]",
        f"Namespaces: [bold]{namespace_count(pods, namespace)}[/bold]",
        f"Nodes: [bold]{node_count}[/bold]",
        f"Pods: [bold]{pod_count}[/bold]",
    ]

    if app.startup_result is not None:
        health_score = app.startup_result.get("health_score", 100)
        if isinstance(health_score, int) and health_score > 0:
            if health_score >= 80:  # noqa: PLR2004
                score_color = "green"
            elif health_score >= 50:  # noqa: PLR2004
                score_color = "yellow"
            else:
                score_color = "red"
            lines.append("")
            lines.append(
                f"Health Score: [bold {score_color}]{health_score}/100[/bold {score_color}]"
            )
        else:
            lines.append("")
            adapter_score = safe_health_score(app.adapter)
            lines.append(f"Health Score: [bold]{adapter_score}/100[/bold]")
    else:
        lines.append("")
        lines.append(f"Health Score: [bold]{safe_health_score(app.adapter)}/100[/bold]")

    lines.extend(
        [
            "",
            f"\U0001f7e2 Running Pods      {running_pod_count(pods)}",
            f"\U0001f7e1 Pending Pods       {pending_pod_count(pods)}",
            f"\U0001f534 Failed Pods        {failed_pod_count(pods)}",
        ]
    )
    lines.extend(format_license_aside_lines())
    lines.append("")
    lines.extend(format_finding_warnings(findings))
    lines.extend(format_suggestion_lines(app, suggestions))

    return lines
