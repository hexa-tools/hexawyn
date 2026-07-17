"""MCP tool — run memory consolidation."""


def run_consolidation(cluster_name: str = "unknown") -> dict[str, object]:
    """Run memory consolidation to group similar incidents into reusable knowledge."""
    from hexawyn.application.ports.driving.run_consolidation.run_consolidation_command import (
        RunConsolidationCommand,
    )
    from hexawyn.application.service.run_consolidation_service import (
        RunConsolidationService,
    )
    from hexawyn.application.use_case.run_consolidation.run_consolidation_use_case import (
        RunConsolidationUseCase,
    )
    from hexawyn.mcp.server import build_consolidation_adapter

    try:
        adapter = build_consolidation_adapter()
        service = RunConsolidationService(consolidation_port=adapter)
        use_case = RunConsolidationUseCase(service=service)
        response = use_case.execute(RunConsolidationCommand(cluster_name=cluster_name))
        return {
            "consolidated": response.groups_found,
            "patterns": [k.pattern for k in response.consolidated],
            "error": None,
        }
    except Exception as exc:
        return {"consolidated": 0, "patterns": [], "error": str(exc)}


def register(mcp: object) -> None:
    mcp.tool()(run_consolidation)  # type: ignore[attr-defined]
