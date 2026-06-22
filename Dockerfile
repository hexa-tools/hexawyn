# ============================================================
# Stage 1: builder — install all Python dependencies
# ============================================================
FROM registry.access.redhat.com/ubi9/python-312 AS builder
WORKDIR /app
# Copy dependency files only (not source code)
# This allows Docker layer caching: deps are only re-installed if pyproject.toml or poetry.lock changes
COPY pyproject.toml poetry.lock ./
# Switch to root — UBI9 Python image runs as non-root by default
USER 0
# Export dependencies to requirements.txt (no dev deps), then install to /install prefix
# The --prefix=/install trick lets us copy just the installed packages to the runtime stage
RUN pip install poetry poetry-plugin-export && \
    poetry export -f requirements.txt -o requirements.txt --without-hashes --without dev && \
    mkdir -p /install && \
    pip install --prefix=/install -r requirements.txt
# ============================================================
# Stage 2: runtime — minimal final image
# ============================================================
FROM registry.access.redhat.com/ubi9/python-312
WORKDIR /app
# Copy compiled packages from builder (no pip, no poetry, no build tools in final image)
COPY --from=builder /install /usr/local
# Copy application source code
COPY src/ ./src/
# src/ layout: Python needs to know where the hexawyn package lives
ENV PYTHONPATH=/app/src
# Red Hat Marketplace certification: non-root user is MANDATORY
# UID 1001 is the standard Red Hat non-root UID
# GID 0 (root group) is required for OpenShift compatibility (arbitrary UID)
USER 0
RUN useradd -r -o -u 1001 -g 0 hexawyn && \
    chown -R 1001:0 /app
USER 1001
# Mount point for kubeconfig (read-only in docker-compose)
VOLUME ["/root/.kube"]
# Mount point for DuckDB persistent memory (~/.hexawyn/memory.db)
VOLUME ["/home/hexawyn/.hexawyn"]
# MCP server port (FastMCP default)
EXPOSE 8000
# Start the FastMCP server
ENTRYPOINT ["python", "-m", "hexawyn.mcp.server"]
