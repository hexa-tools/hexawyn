# ============================================================
# Stage 1: builder — install Python dependencies
# ============================================================
# requirements.txt is generated locally (make deps-export), committed to repo.
# This avoids installing Poetry + poetry-plugin-export during Docker build.
FROM registry.access.redhat.com/ubi9/python-312 AS builder
WORKDIR /app
COPY requirements.txt ./
USER 0
RUN --mount=type=cache,target=/root/.cache/pip \
    mkdir -p /install && \
    pip install --prefix=/install --cache-dir=/root/.cache/pip -r requirements.txt

# ============================================================
# Stage 2: runtime — minimal final image
# ============================================================
FROM registry.access.redhat.com/ubi9/python-312
WORKDIR /app
COPY --from=builder /install /usr/local
COPY src/ ./src/
ENV PYTHONPATH=/app/src
USER 0
RUN useradd -r -o -u 1001 -g 0 hexawyn && \
    chown -R 1001:0 /app
USER 1001
VOLUME ["/root/.kube"]
VOLUME ["/home/hexawyn/.hexawyn"]
EXPOSE 8000
ENTRYPOINT ["python", "-m", "hexawyn.mcp.server"]
