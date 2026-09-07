#!/usr/bin/env bash
#
# hexawyn install script ("curl | bash")
#
# Served from a stable GitHub Releases URL:
#   https://github.com/hexa-tools/hexawyn/releases/latest/download/install.sh
#
# Verify integrity before running (manual, no-pipe alternative):
#   curl -fsSL -o install.sh \
#     https://github.com/hexa-tools/hexawyn/releases/latest/download/install.sh
#   curl -fsSL https://github.com/hexa-tools/hexawyn/releases/latest/download/install.sh.sha256 | sha256sum -c -
#
# hexawyn is Python-native: this installs via pipx (no compiled binary).
#
set -euo pipefail

PACKAGE="hexawyn"
VERSION="0.1.0b20"
MIN_PYTHON_MAJOR=3
MIN_PYTHON_MINOR=12

die() { printf '❌ [hexawyn-install] ERROR: %s\n' "$*" >&2; exit 1; }
log() { printf '→ [hexawyn-install] %s\n' "$*"; }

# ── 1. python3 must be present and of a compatible version ─────────────
command -v python3 >/dev/null 2>&1 \
  || die "python3 is required but not found. Install Python ${MIN_PYTHON_MAJOR}.${MIN_PYTHON_MINOR}+ and re-run."

py_version="$(python3 -c 'import sys; print(f"{sys.version_info[0]}.{sys.version_info[1]}")')"
py_major="${py_version%%.*}"
py_minor="${py_version#*.}"
version_ok=false
if [ "${py_major}" -gt "${MIN_PYTHON_MAJOR}" ]; then
  version_ok=true
elif [ "${py_major}" -eq "${MIN_PYTHON_MAJOR}" ] && [ "${py_minor}" -ge "${MIN_PYTHON_MINOR}" ]; then
  version_ok=true
fi
[ "${version_ok}" = true ] \
  || die "Python ${MIN_PYTHON_MAJOR}.${MIN_PYTHON_MINOR}+ is required (found ${py_version})."

# ── 2. Bootstrap pipx if missing (idempotent) ────────────────────────────
if ! python3 -m pipx --version >/dev/null 2>&1; then
  log "pipx not found — bootstrapping via pip (user site)…"
  python3 -m pip install --user pipx >/dev/null
  python3 -m pipx ensurepath >/dev/null
fi

PIPX=(python3 -m pipx)
if command -v pipx >/dev/null 2>&1; then
  PIPX=(pipx)
fi

# ── 3. Install or upgrade (idempotent, never breaks an existing install) ─
if "${PIPX[@]}" list --short 2>/dev/null | grep -Eq "^${PACKAGE} "; then
  log "upgrading existing ${PACKAGE}…"
  "${PIPX[@]}" upgrade "${PACKAGE}"
else
  log "installing ${PACKAGE}==${VERSION}…"
  "${PIPX[@]}" install "${PACKAGE}==${VERSION}"
fi

# ── 4. Confirm the venv is registered ────────────────────────────────────
if ! "${PIPX[@]}" list --short 2>/dev/null | grep -Eq "^${PACKAGE} "; then
  die "installation did not complete — pipx lists no '${PACKAGE}' application."
fi

printf '\n✅ hexawyn %s installed.\n\nOpen a NEW terminal (so %q is on PATH) and run:\n\n   hexawyn --version\n\n' \
  "${VERSION}" "${HOME}/.local/bin"
