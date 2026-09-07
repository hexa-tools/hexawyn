import asyncio

from hexawyn.application.ports.driven.mcp_discovery_port import MCPDiscoveryPort
from hexawyn.domain.models.mcp_tool import MCPToolRegistry, MCPToolSchema
from hexawyn.mcp.server import mcp


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁMCPDiscoveryAdapterǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁMCPDiscoveryAdapterǁdiscover__mutmut: MutantDict = {}  # type: ignore


class MCPDiscoveryAdapter(MCPDiscoveryPort):
    """Discovers MCP tools from the local FastMCP server instance."""

    @_mutmut_mutated(mutants_xǁMCPDiscoveryAdapterǁ__init____mutmut)
    def __init__(self) -> None:
        self._cached: MCPToolRegistry | None = None

    def xǁMCPDiscoveryAdapterǁ__init____mutmut_orig(self) -> None:
        self._cached: MCPToolRegistry | None = None

    def xǁMCPDiscoveryAdapterǁ__init____mutmut_1(self) -> None:
        self._cached: MCPToolRegistry | None = ""

    @_mutmut_mutated(mutants_xǁMCPDiscoveryAdapterǁdiscover__mutmut)
    def discover(self) -> MCPToolRegistry:
        if self._cached is not None:
            return self._cached

        try:
            raw_tools = asyncio.run(mcp.list_tools())
            self._cached = MCPToolRegistry(
                tools=[
                    MCPToolSchema(
                        name=t.name,
                        description=t.description or "",
                        input_schema=getattr(t, "inputSchema", {}),
                    )
                    for t in raw_tools
                ]
            )
        except Exception:
            self._cached = MCPToolRegistry()

        return self._cached

    def xǁMCPDiscoveryAdapterǁdiscover__mutmut_orig(self) -> MCPToolRegistry:
        if self._cached is not None:
            return self._cached

        try:
            raw_tools = asyncio.run(mcp.list_tools())
            self._cached = MCPToolRegistry(
                tools=[
                    MCPToolSchema(
                        name=t.name,
                        description=t.description or "",
                        input_schema=getattr(t, "inputSchema", {}),
                    )
                    for t in raw_tools
                ]
            )
        except Exception:
            self._cached = MCPToolRegistry()

        return self._cached

    def xǁMCPDiscoveryAdapterǁdiscover__mutmut_1(self) -> MCPToolRegistry:
        if self._cached is None:
            return self._cached

        try:
            raw_tools = asyncio.run(mcp.list_tools())
            self._cached = MCPToolRegistry(
                tools=[
                    MCPToolSchema(
                        name=t.name,
                        description=t.description or "",
                        input_schema=getattr(t, "inputSchema", {}),
                    )
                    for t in raw_tools
                ]
            )
        except Exception:
            self._cached = MCPToolRegistry()

        return self._cached

    def xǁMCPDiscoveryAdapterǁdiscover__mutmut_2(self) -> MCPToolRegistry:
        if self._cached is not None:
            return self._cached

        try:
            raw_tools = None
            self._cached = MCPToolRegistry(
                tools=[
                    MCPToolSchema(
                        name=t.name,
                        description=t.description or "",
                        input_schema=getattr(t, "inputSchema", {}),
                    )
                    for t in raw_tools
                ]
            )
        except Exception:
            self._cached = MCPToolRegistry()

        return self._cached

    def xǁMCPDiscoveryAdapterǁdiscover__mutmut_3(self) -> MCPToolRegistry:
        if self._cached is not None:
            return self._cached

        try:
            raw_tools = asyncio.run(None)
            self._cached = MCPToolRegistry(
                tools=[
                    MCPToolSchema(
                        name=t.name,
                        description=t.description or "",
                        input_schema=getattr(t, "inputSchema", {}),
                    )
                    for t in raw_tools
                ]
            )
        except Exception:
            self._cached = MCPToolRegistry()

        return self._cached

    def xǁMCPDiscoveryAdapterǁdiscover__mutmut_4(self) -> MCPToolRegistry:
        if self._cached is not None:
            return self._cached

        try:
            raw_tools = asyncio.run(mcp.list_tools())
            self._cached = None
        except Exception:
            self._cached = MCPToolRegistry()

        return self._cached

    def xǁMCPDiscoveryAdapterǁdiscover__mutmut_5(self) -> MCPToolRegistry:
        if self._cached is not None:
            return self._cached

        try:
            raw_tools = asyncio.run(mcp.list_tools())
            self._cached = MCPToolRegistry(
                tools=None
            )
        except Exception:
            self._cached = MCPToolRegistry()

        return self._cached

    def xǁMCPDiscoveryAdapterǁdiscover__mutmut_6(self) -> MCPToolRegistry:
        if self._cached is not None:
            return self._cached

        try:
            raw_tools = asyncio.run(mcp.list_tools())
            self._cached = MCPToolRegistry(
                tools=[
                    MCPToolSchema(
                        name=None,
                        description=t.description or "",
                        input_schema=getattr(t, "inputSchema", {}),
                    )
                    for t in raw_tools
                ]
            )
        except Exception:
            self._cached = MCPToolRegistry()

        return self._cached

    def xǁMCPDiscoveryAdapterǁdiscover__mutmut_7(self) -> MCPToolRegistry:
        if self._cached is not None:
            return self._cached

        try:
            raw_tools = asyncio.run(mcp.list_tools())
            self._cached = MCPToolRegistry(
                tools=[
                    MCPToolSchema(
                        name=t.name,
                        description=None,
                        input_schema=getattr(t, "inputSchema", {}),
                    )
                    for t in raw_tools
                ]
            )
        except Exception:
            self._cached = MCPToolRegistry()

        return self._cached

    def xǁMCPDiscoveryAdapterǁdiscover__mutmut_8(self) -> MCPToolRegistry:
        if self._cached is not None:
            return self._cached

        try:
            raw_tools = asyncio.run(mcp.list_tools())
            self._cached = MCPToolRegistry(
                tools=[
                    MCPToolSchema(
                        name=t.name,
                        description=t.description or "",
                        input_schema=None,
                    )
                    for t in raw_tools
                ]
            )
        except Exception:
            self._cached = MCPToolRegistry()

        return self._cached

    def xǁMCPDiscoveryAdapterǁdiscover__mutmut_9(self) -> MCPToolRegistry:
        if self._cached is not None:
            return self._cached

        try:
            raw_tools = asyncio.run(mcp.list_tools())
            self._cached = MCPToolRegistry(
                tools=[
                    MCPToolSchema(
                        description=t.description or "",
                        input_schema=getattr(t, "inputSchema", {}),
                    )
                    for t in raw_tools
                ]
            )
        except Exception:
            self._cached = MCPToolRegistry()

        return self._cached

    def xǁMCPDiscoveryAdapterǁdiscover__mutmut_10(self) -> MCPToolRegistry:
        if self._cached is not None:
            return self._cached

        try:
            raw_tools = asyncio.run(mcp.list_tools())
            self._cached = MCPToolRegistry(
                tools=[
                    MCPToolSchema(
                        name=t.name,
                        input_schema=getattr(t, "inputSchema", {}),
                    )
                    for t in raw_tools
                ]
            )
        except Exception:
            self._cached = MCPToolRegistry()

        return self._cached

    def xǁMCPDiscoveryAdapterǁdiscover__mutmut_11(self) -> MCPToolRegistry:
        if self._cached is not None:
            return self._cached

        try:
            raw_tools = asyncio.run(mcp.list_tools())
            self._cached = MCPToolRegistry(
                tools=[
                    MCPToolSchema(
                        name=t.name,
                        description=t.description or "",
                        )
                    for t in raw_tools
                ]
            )
        except Exception:
            self._cached = MCPToolRegistry()

        return self._cached

    def xǁMCPDiscoveryAdapterǁdiscover__mutmut_12(self) -> MCPToolRegistry:
        if self._cached is not None:
            return self._cached

        try:
            raw_tools = asyncio.run(mcp.list_tools())
            self._cached = MCPToolRegistry(
                tools=[
                    MCPToolSchema(
                        name=t.name,
                        description=t.description and "",
                        input_schema=getattr(t, "inputSchema", {}),
                    )
                    for t in raw_tools
                ]
            )
        except Exception:
            self._cached = MCPToolRegistry()

        return self._cached

    def xǁMCPDiscoveryAdapterǁdiscover__mutmut_13(self) -> MCPToolRegistry:
        if self._cached is not None:
            return self._cached

        try:
            raw_tools = asyncio.run(mcp.list_tools())
            self._cached = MCPToolRegistry(
                tools=[
                    MCPToolSchema(
                        name=t.name,
                        description=t.description or "XXXX",
                        input_schema=getattr(t, "inputSchema", {}),
                    )
                    for t in raw_tools
                ]
            )
        except Exception:
            self._cached = MCPToolRegistry()

        return self._cached

    def xǁMCPDiscoveryAdapterǁdiscover__mutmut_14(self) -> MCPToolRegistry:
        if self._cached is not None:
            return self._cached

        try:
            raw_tools = asyncio.run(mcp.list_tools())
            self._cached = MCPToolRegistry(
                tools=[
                    MCPToolSchema(
                        name=t.name,
                        description=t.description or "",
                        input_schema=getattr(None, "inputSchema", {}),
                    )
                    for t in raw_tools
                ]
            )
        except Exception:
            self._cached = MCPToolRegistry()

        return self._cached

    def xǁMCPDiscoveryAdapterǁdiscover__mutmut_15(self) -> MCPToolRegistry:
        if self._cached is not None:
            return self._cached

        try:
            raw_tools = asyncio.run(mcp.list_tools())
            self._cached = MCPToolRegistry(
                tools=[
                    MCPToolSchema(
                        name=t.name,
                        description=t.description or "",
                        input_schema=getattr(t, None, {}),
                    )
                    for t in raw_tools
                ]
            )
        except Exception:
            self._cached = MCPToolRegistry()

        return self._cached

    def xǁMCPDiscoveryAdapterǁdiscover__mutmut_16(self) -> MCPToolRegistry:
        if self._cached is not None:
            return self._cached

        try:
            raw_tools = asyncio.run(mcp.list_tools())
            self._cached = MCPToolRegistry(
                tools=[
                    MCPToolSchema(
                        name=t.name,
                        description=t.description or "",
                        input_schema=getattr(t, "inputSchema", None),
                    )
                    for t in raw_tools
                ]
            )
        except Exception:
            self._cached = MCPToolRegistry()

        return self._cached

    def xǁMCPDiscoveryAdapterǁdiscover__mutmut_17(self) -> MCPToolRegistry:
        if self._cached is not None:
            return self._cached

        try:
            raw_tools = asyncio.run(mcp.list_tools())
            self._cached = MCPToolRegistry(
                tools=[
                    MCPToolSchema(
                        name=t.name,
                        description=t.description or "",
                        input_schema=getattr("inputSchema", {}),
                    )
                    for t in raw_tools
                ]
            )
        except Exception:
            self._cached = MCPToolRegistry()

        return self._cached

    def xǁMCPDiscoveryAdapterǁdiscover__mutmut_18(self) -> MCPToolRegistry:
        if self._cached is not None:
            return self._cached

        try:
            raw_tools = asyncio.run(mcp.list_tools())
            self._cached = MCPToolRegistry(
                tools=[
                    MCPToolSchema(
                        name=t.name,
                        description=t.description or "",
                        input_schema=getattr(t, {}),
                    )
                    for t in raw_tools
                ]
            )
        except Exception:
            self._cached = MCPToolRegistry()

        return self._cached

    def xǁMCPDiscoveryAdapterǁdiscover__mutmut_19(self) -> MCPToolRegistry:
        if self._cached is not None:
            return self._cached

        try:
            raw_tools = asyncio.run(mcp.list_tools())
            self._cached = MCPToolRegistry(
                tools=[
                    MCPToolSchema(
                        name=t.name,
                        description=t.description or "",
                        input_schema=getattr(t, "inputSchema", ),
                    )
                    for t in raw_tools
                ]
            )
        except Exception:
            self._cached = MCPToolRegistry()

        return self._cached

    def xǁMCPDiscoveryAdapterǁdiscover__mutmut_20(self) -> MCPToolRegistry:
        if self._cached is not None:
            return self._cached

        try:
            raw_tools = asyncio.run(mcp.list_tools())
            self._cached = MCPToolRegistry(
                tools=[
                    MCPToolSchema(
                        name=t.name,
                        description=t.description or "",
                        input_schema=getattr(t, "XXinputSchemaXX", {}),
                    )
                    for t in raw_tools
                ]
            )
        except Exception:
            self._cached = MCPToolRegistry()

        return self._cached

    def xǁMCPDiscoveryAdapterǁdiscover__mutmut_21(self) -> MCPToolRegistry:
        if self._cached is not None:
            return self._cached

        try:
            raw_tools = asyncio.run(mcp.list_tools())
            self._cached = MCPToolRegistry(
                tools=[
                    MCPToolSchema(
                        name=t.name,
                        description=t.description or "",
                        input_schema=getattr(t, "inputschema", {}),
                    )
                    for t in raw_tools
                ]
            )
        except Exception:
            self._cached = MCPToolRegistry()

        return self._cached

    def xǁMCPDiscoveryAdapterǁdiscover__mutmut_22(self) -> MCPToolRegistry:
        if self._cached is not None:
            return self._cached

        try:
            raw_tools = asyncio.run(mcp.list_tools())
            self._cached = MCPToolRegistry(
                tools=[
                    MCPToolSchema(
                        name=t.name,
                        description=t.description or "",
                        input_schema=getattr(t, "INPUTSCHEMA", {}),
                    )
                    for t in raw_tools
                ]
            )
        except Exception:
            self._cached = MCPToolRegistry()

        return self._cached

    def xǁMCPDiscoveryAdapterǁdiscover__mutmut_23(self) -> MCPToolRegistry:
        if self._cached is not None:
            return self._cached

        try:
            raw_tools = asyncio.run(mcp.list_tools())
            self._cached = MCPToolRegistry(
                tools=[
                    MCPToolSchema(
                        name=t.name,
                        description=t.description or "",
                        input_schema=getattr(t, "inputSchema", {}),
                    )
                    for t in raw_tools
                ]
            )
        except Exception:
            self._cached = None

        return self._cached

mutants_xǁMCPDiscoveryAdapterǁ__init____mutmut['_mutmut_orig'] = MCPDiscoveryAdapter.xǁMCPDiscoveryAdapterǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁMCPDiscoveryAdapterǁ__init____mutmut['xǁMCPDiscoveryAdapterǁ__init____mutmut_1'] = MCPDiscoveryAdapter.xǁMCPDiscoveryAdapterǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁMCPDiscoveryAdapterǁdiscover__mutmut['_mutmut_orig'] = MCPDiscoveryAdapter.xǁMCPDiscoveryAdapterǁdiscover__mutmut_orig # type: ignore # mutmut generated
mutants_xǁMCPDiscoveryAdapterǁdiscover__mutmut['xǁMCPDiscoveryAdapterǁdiscover__mutmut_1'] = MCPDiscoveryAdapter.xǁMCPDiscoveryAdapterǁdiscover__mutmut_1 # type: ignore # mutmut generated
mutants_xǁMCPDiscoveryAdapterǁdiscover__mutmut['xǁMCPDiscoveryAdapterǁdiscover__mutmut_2'] = MCPDiscoveryAdapter.xǁMCPDiscoveryAdapterǁdiscover__mutmut_2 # type: ignore # mutmut generated
mutants_xǁMCPDiscoveryAdapterǁdiscover__mutmut['xǁMCPDiscoveryAdapterǁdiscover__mutmut_3'] = MCPDiscoveryAdapter.xǁMCPDiscoveryAdapterǁdiscover__mutmut_3 # type: ignore # mutmut generated
mutants_xǁMCPDiscoveryAdapterǁdiscover__mutmut['xǁMCPDiscoveryAdapterǁdiscover__mutmut_4'] = MCPDiscoveryAdapter.xǁMCPDiscoveryAdapterǁdiscover__mutmut_4 # type: ignore # mutmut generated
mutants_xǁMCPDiscoveryAdapterǁdiscover__mutmut['xǁMCPDiscoveryAdapterǁdiscover__mutmut_5'] = MCPDiscoveryAdapter.xǁMCPDiscoveryAdapterǁdiscover__mutmut_5 # type: ignore # mutmut generated
mutants_xǁMCPDiscoveryAdapterǁdiscover__mutmut['xǁMCPDiscoveryAdapterǁdiscover__mutmut_6'] = MCPDiscoveryAdapter.xǁMCPDiscoveryAdapterǁdiscover__mutmut_6 # type: ignore # mutmut generated
mutants_xǁMCPDiscoveryAdapterǁdiscover__mutmut['xǁMCPDiscoveryAdapterǁdiscover__mutmut_7'] = MCPDiscoveryAdapter.xǁMCPDiscoveryAdapterǁdiscover__mutmut_7 # type: ignore # mutmut generated
mutants_xǁMCPDiscoveryAdapterǁdiscover__mutmut['xǁMCPDiscoveryAdapterǁdiscover__mutmut_8'] = MCPDiscoveryAdapter.xǁMCPDiscoveryAdapterǁdiscover__mutmut_8 # type: ignore # mutmut generated
mutants_xǁMCPDiscoveryAdapterǁdiscover__mutmut['xǁMCPDiscoveryAdapterǁdiscover__mutmut_9'] = MCPDiscoveryAdapter.xǁMCPDiscoveryAdapterǁdiscover__mutmut_9 # type: ignore # mutmut generated
mutants_xǁMCPDiscoveryAdapterǁdiscover__mutmut['xǁMCPDiscoveryAdapterǁdiscover__mutmut_10'] = MCPDiscoveryAdapter.xǁMCPDiscoveryAdapterǁdiscover__mutmut_10 # type: ignore # mutmut generated
mutants_xǁMCPDiscoveryAdapterǁdiscover__mutmut['xǁMCPDiscoveryAdapterǁdiscover__mutmut_11'] = MCPDiscoveryAdapter.xǁMCPDiscoveryAdapterǁdiscover__mutmut_11 # type: ignore # mutmut generated
mutants_xǁMCPDiscoveryAdapterǁdiscover__mutmut['xǁMCPDiscoveryAdapterǁdiscover__mutmut_12'] = MCPDiscoveryAdapter.xǁMCPDiscoveryAdapterǁdiscover__mutmut_12 # type: ignore # mutmut generated
mutants_xǁMCPDiscoveryAdapterǁdiscover__mutmut['xǁMCPDiscoveryAdapterǁdiscover__mutmut_13'] = MCPDiscoveryAdapter.xǁMCPDiscoveryAdapterǁdiscover__mutmut_13 # type: ignore # mutmut generated
mutants_xǁMCPDiscoveryAdapterǁdiscover__mutmut['xǁMCPDiscoveryAdapterǁdiscover__mutmut_14'] = MCPDiscoveryAdapter.xǁMCPDiscoveryAdapterǁdiscover__mutmut_14 # type: ignore # mutmut generated
mutants_xǁMCPDiscoveryAdapterǁdiscover__mutmut['xǁMCPDiscoveryAdapterǁdiscover__mutmut_15'] = MCPDiscoveryAdapter.xǁMCPDiscoveryAdapterǁdiscover__mutmut_15 # type: ignore # mutmut generated
mutants_xǁMCPDiscoveryAdapterǁdiscover__mutmut['xǁMCPDiscoveryAdapterǁdiscover__mutmut_16'] = MCPDiscoveryAdapter.xǁMCPDiscoveryAdapterǁdiscover__mutmut_16 # type: ignore # mutmut generated
mutants_xǁMCPDiscoveryAdapterǁdiscover__mutmut['xǁMCPDiscoveryAdapterǁdiscover__mutmut_17'] = MCPDiscoveryAdapter.xǁMCPDiscoveryAdapterǁdiscover__mutmut_17 # type: ignore # mutmut generated
mutants_xǁMCPDiscoveryAdapterǁdiscover__mutmut['xǁMCPDiscoveryAdapterǁdiscover__mutmut_18'] = MCPDiscoveryAdapter.xǁMCPDiscoveryAdapterǁdiscover__mutmut_18 # type: ignore # mutmut generated
mutants_xǁMCPDiscoveryAdapterǁdiscover__mutmut['xǁMCPDiscoveryAdapterǁdiscover__mutmut_19'] = MCPDiscoveryAdapter.xǁMCPDiscoveryAdapterǁdiscover__mutmut_19 # type: ignore # mutmut generated
mutants_xǁMCPDiscoveryAdapterǁdiscover__mutmut['xǁMCPDiscoveryAdapterǁdiscover__mutmut_20'] = MCPDiscoveryAdapter.xǁMCPDiscoveryAdapterǁdiscover__mutmut_20 # type: ignore # mutmut generated
mutants_xǁMCPDiscoveryAdapterǁdiscover__mutmut['xǁMCPDiscoveryAdapterǁdiscover__mutmut_21'] = MCPDiscoveryAdapter.xǁMCPDiscoveryAdapterǁdiscover__mutmut_21 # type: ignore # mutmut generated
mutants_xǁMCPDiscoveryAdapterǁdiscover__mutmut['xǁMCPDiscoveryAdapterǁdiscover__mutmut_22'] = MCPDiscoveryAdapter.xǁMCPDiscoveryAdapterǁdiscover__mutmut_22 # type: ignore # mutmut generated
mutants_xǁMCPDiscoveryAdapterǁdiscover__mutmut['xǁMCPDiscoveryAdapterǁdiscover__mutmut_23'] = MCPDiscoveryAdapter.xǁMCPDiscoveryAdapterǁdiscover__mutmut_23 # type: ignore # mutmut generated
