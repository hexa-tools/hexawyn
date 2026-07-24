#!/usr/bin/env python3
"""
Migration script v3 — handles all edge cases.
"""

from __future__ import annotations

import re
import shutil
from pathlib import Path

PROJECT_ROOT = Path("/home/djepeno/sites/hexawyn")
SRC = PROJECT_ROOT / "src" / "hexawyn"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def delete_dir(path: Path) -> None:
    if path.is_dir():
        shutil.rmtree(path)


def delete_file(path: Path) -> None:
    if path.exists():
        path.unlink()


def find_class_and_method(service_content: str) -> tuple[str | None, str | None]:
    """Find the service class name and its MAIN public method (skips __init__ and private methods)."""
    class_match = re.search(r"class (\w+)\(.*ServicePort\):", service_content)
    if not class_match:
        return None, None

    svc_class = class_match.group(1)
    class_start = service_content.index(f"class {svc_class}")
    class_body = service_content[class_start:]

    # Join multi-line continuation lines (indented lines that aren't 'def')
    lines = class_body.split("\n")
    joined = []
    for line in lines:
        if line and line[0].isspace() and not re.match(r" {4}def ", line):
            joined.append(line.strip())
        else:
            joined.append("\n" + line)
    normalized = "".join(joined)
    normalized = re.sub(r"\n+", "\n", normalized)

    all_methods = re.findall(r"    def (\w+)", normalized)

    main_method = None
    for m in all_methods:
        if m != "__init__" and not m.startswith("_"):
            main_method = m
            break

    return svc_class, main_method


def camel(name: str) -> str:
    return "".join(p.capitalize() for p in name.split("_"))


def _find_init_block(class_lines: list[str]) -> tuple[list[str], list[str]]:
    """Returns (init_signature_lines, init_body_lines) or (['    pass'], [])."""
    init_start = None
    for i, line in enumerate(class_lines):
        if "def __init__" in line:
            init_start = i
            break

    if init_start is None:
        return ["        pass"], []

    # Collect init signature (multi-line possible)
    init_sig = []
    init_sig_end = init_start
    for i in range(init_start, len(class_lines)):
        line = class_lines[i]
        init_sig.append(line)
        if ":" in line and line.rstrip().endswith(":"):
            init_sig_end = i
            break

    # Find init body end (next method)
    init_body_end = len(class_lines)
    for i in range(init_sig_end + 1, len(class_lines)):
        if re.match(r"    def \w+", class_lines[i]):
            init_body_end = i
            break

    init_body = class_lines[init_sig_end + 1 : init_body_end]
    return init_sig, init_body


def _find_method_block(class_lines: list[str], method_name: str) -> tuple[list[str], list[str]] | None:
    """Returns (method_lines, remaining_methods) or None."""
    method_start = None
    for i, line in enumerate(class_lines):
        if f"def {method_name}" in line:
            method_start = i
            break

    if method_start is None:
        return None

    method_end = len(class_lines)
    for i in range(method_start + 1, len(class_lines)):
        if re.match(r"    def \w+", class_lines[i]):
            method_end = i
            break

    method_lines = class_lines[method_start:method_end]
    remaining = class_lines[method_end:]
    return method_lines, remaining


def migrate_use_case_file(use_case_name: str, service_filename: str) -> bool:
    service_path = SRC / "application" / "service" / service_filename
    if not service_path.exists():
        print(f"  SKIP: no service file at {service_path}")
        return False

    svc_content = read(service_path)
    svc_class, svc_method = find_class_and_method(svc_content)

    if not svc_class or not svc_method:
        print(f"  WARN: class={svc_class}, method={svc_method} in {service_path}")
        return False

    uc_class = camel(use_case_name) + "UseCase"
    cmd_class = camel(use_case_name) + "Command"
    rsp_class = camel(use_case_name) + "Response"

    print(f"  Class: {svc_class}, method: {svc_method}")

    # Split into parts
    class_idx = svc_content.index(f"class {svc_class}")
    before_class = svc_content[:class_idx]

    lines_all = svc_content.split("\n")
    class_line = None
    for i, line in enumerate(lines_all):
        if f"class {svc_class}" in line:
            class_line = i
            break

    end_class = len(lines_all)
    for i in range(class_line + 1, len(lines_all)):
        line = lines_all[i]
        if line and not line[0].isspace():
            end_class = i
            break

    class_lines = lines_all[class_line:end_class]
    post_class_lines = lines_all[end_class:]

    # Extract blocks
    init_sig, init_body = _find_init_block(class_lines)
    method_result = _find_method_block(class_lines, svc_method)
    if method_result is None:
        print(f"  WARN: method {svc_method} not found")
        return False
    method_lines, remaining_methods = method_result

    # Build new use_case
    new_lines = []

    # Filter imports
    service_port_tag = f"ports.driving.{use_case_name}.{use_case_name}_service_port"
    command_old = f"ports.driving.{use_case_name}.{use_case_name}_command"
    response_old = f"ports.driving.{use_case_name}.{use_case_name}_response"

    for line in before_class.split("\n"):
        if service_port_tag in line or command_old in line or response_old in line:
            continue
        new_lines.append(line)

    new_lines.append(f"from hexawyn.application.use_case.{use_case_name}.command import {cmd_class}")
    new_lines.append(f"from hexawyn.application.use_case.{use_case_name}.response import {rsp_class}")
    new_lines.append("")
    new_lines.append("")

    # Class
    new_lines.append(f"class {uc_class}:")
    for line in init_sig:
        new_lines.append(line)
    for line in init_body:
        new_lines.append(line)
    if not any(s.strip() for s in init_body):
        new_lines.append("        pass")
    new_lines.append("")

    # execute method
    exec_first = method_lines[0].replace(svc_method, "execute")
    new_lines.append(exec_first)
    for line in method_lines[1:]:
        new_lines.append(line)

    # Remaining
    if remaining_methods:
        new_lines.append("")
        for line in remaining_methods:
            new_lines.append(line)

    # Post-class helpers
    start = 0
    while start < len(post_class_lines) and not post_class_lines[start].strip():
        start += 1
    post = post_class_lines[start:]
    if post:
        new_lines.append("")
        for line in post:
            new_lines.append(line)

    content = "\n".join(new_lines)
    content = re.sub(r"[ \t]+$", "", content, flags=re.MULTILINE)
    content = re.sub(r"\n{3,}", "\n\n", content)

    new_uc_path = SRC / "application" / "use_case" / use_case_name / f"{use_case_name}_use_case.py"
    write(new_uc_path, content)
    print(f"  Wrote: {new_uc_path.relative_to(PROJECT_ROOT)}")
    return True


def migrate_mcp_tool(use_case_name: str, mcp_filename: str | None = None) -> None:
    tool_path = SRC / "mcp" / "tools" / (mcp_filename or f"{use_case_name}.py")
    if not tool_path.exists():
        print(f"  WARN: MCP tool not found: {tool_path}")
        return

    content = read(tool_path)
    uc_class = camel(use_case_name) + "UseCase"
    svc_module = f"hexawyn.application.service.{use_case_name}_service"

    lines = content.split("\n")
    new_lines = []

    for line in lines:
        if svc_module in line and "import" in line:
            continue

        if f"ports.driving.{use_case_name}.{use_case_name}_command import" in line:
            continue

        stripped = line.strip()

        # Remove service instantiation lines
        if re.match(rf"\w*\s*=\s*\w+Service\(.*\)", stripped):
            continue

        # Fix collapsed: UseCase(service=Service(port=a)) → UseCase(port=a)
        line = re.sub(rf"service=\w+Service\(port=(\w+)\)", r"port=\1", line)

        if f"{uc_class}(service=service)" in line:
            line = line.replace(f"{uc_class}(service=service)", f"{uc_class}(port=adapter)")
        if f"{uc_class}(service=svc)" in line:
            line = line.replace(f"{uc_class}(service=svc)", f"{uc_class}(port=adapter)")

        new_lines.append(line)

    write(tool_path, "\n".join(new_lines))
    print(f"  Updated: {tool_path.relative_to(PROJECT_ROOT)}")


def copy_command_response(use_case_name: str) -> None:
    ports_dir = SRC / "application" / "ports" / "driving" / use_case_name
    use_case_dir = SRC / "application" / "use_case" / use_case_name

    for suffix in ["_command.py", "_response.py"]:
        src = ports_dir / f"{use_case_name}{suffix}"
        if src.exists():
            dest = use_case_dir / suffix.lstrip("_")
            if not dest.exists() or read(src) != read(dest):
                write(dest, read(src))
                print(f"  Copied: {dest.relative_to(PROJECT_ROOT)}")


def cleanup(use_case_name: str, service_filename: str) -> None:
    service_path = SRC / "application" / "service" / service_filename
    ports_dir = SRC / "application" / "ports" / "driving" / use_case_name
    if service_path.exists():
        delete_file(service_path)
        print(f"  Deleted: {service_path.relative_to(PROJECT_ROOT)}")
    if ports_dir.exists():
        delete_dir(ports_dir)
        print(f"  Deleted: {ports_dir.relative_to(PROJECT_ROOT)}")


def migrate_one(use_case_name: str, service_filename: str, mcp_filename: str | None = None) -> None:
    print(f"\n{'='*60}")
    print(f"Migrating: {use_case_name} (svc: {service_filename})")

    copy_command_response(use_case_name)
    ok = migrate_use_case_file(use_case_name, service_filename)
    if ok:
        migrate_mcp_tool(use_case_name, mcp_filename)
        cleanup(use_case_name, service_filename)
    else:
        print(f"  ⚠ Skipped cleanup for {use_case_name}")


# ── Remaining migrations with known issues ──────────────────────

REMAINING = [
    ("detect_outdated_helm_releases", "detect_outdated_helm_releases_service.py"),
    ("estimate_rightsizing_savings", "estimate_rightsizing_savings_service.py"),
    ("forecast_cost", "forecast_cost_service.py"),
    ("live_topology_mapper", "live_topology_mapper_service.py"),
    ("detect_over_provisioned_namespaces", "detect_over_provisioned_namespaces_service.py"),
    ("compute_monthly_incident_report", "compute_monthly_incident_report_service.py"),
    ("list_pipeline_runs_in_namespace", "list_pipeline_runs_in_namespace_service.py"),
    ("estimate_cost_saving", "estimate_cost_saving_service.py"),
    ("configuration_drift_detection", "configuration_drift_detection_service.py"),
    ("detect_container_image_drift", "container_image_drift_service.py",
     "container_image_drift_detection.py"),  # MCP tool has different name
    ("summarize_namespace_events", "summarize_namespace_events_service.py"),
    ("analyze_advanced_namespace_events", "advanced_namespace_event_analytics_service.py",
     "analyze_advanced_namespace_events.py"),  # MCP tool name
]


def main() -> None:
    for args in REMAINING:
        try:
            migrate_one(*args)
        except Exception as exc:
            print(f"  ERROR: {exc}")
            import traceback
            traceback.print_exc()

    print(f"\n{'='*60}")
    print("Remaining migrations complete.")


if __name__ == "__main__":
    main()
