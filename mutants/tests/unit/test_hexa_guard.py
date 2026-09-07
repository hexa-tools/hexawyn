"""Tests for the hexa_guard.py layer-boundary rules after the
adapters → infrastructure/adapters/ relocation.

hexa_guard.py reads one JSON payload (Write/Edit event) from stdin and prints
{"decision": "block"|"approve"}. These tests exercise the RULE 19 and RULE 5
semantics through a subprocess, mirroring how the hook is invoked.
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

GUARD = Path(__file__).resolve().parents[2] / "hexa_guard.py"


def _run_guard(file_path: str, content: str) -> str:
    payload = {
        "tool_name": "Write",
        "tool_input": {"file_path": file_path, "content": content},
    }
    proc = subprocess.run(
        [sys.executable, str(GUARD)],
        input=json.dumps(payload),
        capture_output=True,
        text=True,
        check=False,
    )
    result = json.loads(proc.stdout)
    return result["decision"]


class TestLayerBoundariesAfterRelocation:
    def test_adapters_may_import_infrastructure(self) -> None:
        decision = _run_guard(
            "src/hexawyn/infrastructure/adapters/secondary/mock/errors.py",
            "from hexawyn.infrastructure.memory.sanitizer import clean_text\n",
        )

        assert decision == "approve"

    def test_adapters_may_import_application_ports(self) -> None:
        decision = _run_guard(
            "src/hexawyn/infrastructure/adapters/secondary/mock/errors.py",
            "from hexawyn.application.ports.driven.fleet_health_port import FleetHealthPort\n",
        )

        assert decision == "approve"

    def test_adapters_cannot_import_domain_models_directly(self) -> None:
        decision = _run_guard(
            "src/hexawyn/infrastructure/adapters/secondary/mock/errors.py",
            "from hexawyn.domain.models.fleet_health import ClusterRawMetrics\n",
        )

        assert decision == "block"

    def test_pure_infrastructure_cannot_import_adapters(self) -> None:
        decision = _run_guard(
            "src/hexawyn/infrastructure/memory/errors.py",
            # noqa: E501 - long module path exercised through the guard subprocess
            "from hexawyn.infrastructure.adapters.secondary.adapter_factory import AdapterFactory\n",  # noqa: E501
        )

        assert decision == "block"

    def test_domain_cannot_import_infrastructure(self) -> None:
        decision = _run_guard(
            "src/hexawyn/domain/services/errors.py",
            "from hexawyn.infrastructure.memory.sanitizer import clean_text\n",
        )

        assert decision == "block"

    def test_infrastructure_may_import_domain_errors(self) -> None:
        decision = _run_guard(
            "src/hexawyn/infrastructure/memory/errors.py",
            "from hexawyn.domain.errors import HexawynError\n",
        )

        assert decision == "approve"
