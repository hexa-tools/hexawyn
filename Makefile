# ═══════════════════════════════════════════════════════════
#  hexawyn — Makefile
# ═══════════════════════════════════════════════════════════

# ─────────────────────────────────────
#  Variables
# ─────────────────────────────────────

POETRY  := poetry
PYTHON  := $(POETRY) run python
PYTEST  := $(POETRY) run pytest
RUFF    := $(POETRY) run ruff
MYPY    := $(POETRY) run mypy

DOCKER_IMAGE := hexawyn

ifneq (,$(wildcard .env))
include .env
export
endif

# ─────────────────────────────────────
#  Dev setup
# ─────────────────────────────────────

.PHONY: install deps-export

install:
	@echo "📦 Installing all dependencies..."
	$(POETRY) install --with dev
	@echo "✅ Dependencies installed"

deps-export:
	@echo "📋 Exporting requirements.txt from Poetry..."
	$(POETRY) export -f requirements.txt --output requirements.txt --without-hashes --without dev
	@echo "✅ requirements.txt updated — commit this file"

# ─────────────────────────────────────
#  Code quality
# ─────────────────────────────────────

.PHONY: lint format format-check type-check check

lint:
	@echo "🔍 Linting Python with ruff..."
	$(RUFF) check src/ tests/
	@echo "✅ Lint passed"

format:
	@echo "🎨 Formatting Python with ruff..."
	$(RUFF) format src/ tests/
	@echo "✅ Formatting done"

format-check:
	@echo "📐 Checking Python formatting with ruff..."
	$(RUFF) format --check src/ tests/
	@echo "✅ Format check passed"

type-check:
	@echo "🔎 Running mypy strict type check..."
	$(MYPY) src/hexawyn/
	@echo "✅ Type check passed"

check:
	@echo "🔍 Running all quality checks..."
	@echo ""
	@$(MAKE) lint
	@$(MAKE) format-check
	@$(MAKE) type-check
	@echo ""
	@echo "✅ All checks passed"

# ─────────────────────────────────────
#  Tests
# ─────────────────────────────────────

.PHONY: test test-integration test-e2e test-e2e-ci test-all coverage update-badge

test:
	@echo "🧪 Running unit tests (parallel)..."
	$(PYTEST) tests/unit/ -q --tb=short -n auto
	@echo "✅ Unit tests passed"

test-integration:
	@echo "🔬 Running integration tests (real DuckDB, demo adapter)..."
	$(PYTEST) tests/integration/ -v -m integration
	@echo "✅ Integration tests passed"

test-e2e:
	@echo "🧪 Running E2E tests (real k3d cluster)..."
	@k3d kubeconfig get $(CLUSTER_NAME) > /tmp/k3d-$(CLUSTER_NAME).yaml 2>/dev/null || true
	KUBECONFIG=/tmp/k3d-$(CLUSTER_NAME).yaml $(PYTEST) tests/e2e/ -v -m e2e --strict-markers --tb=short
	@echo "✅ E2E tests passed"

test-e2e-ci:
	@echo "🚀 Full E2E cycle: create cluster + load fixtures + test + teardown..."
	@$(MAKE) cluster-up
	@$(MAKE) cluster-load
	@$(PYTEST) tests/e2e/ -v -m e2e --strict-markers --tb=short; \
	EXIT_CODE=$$?; \
	$(MAKE) cluster-down; \
	exit $$EXIT_CODE

test-all:
	@echo "🧪 Running all tests (unit + integration)..."
	$(PYTEST) tests/unit/ tests/integration/ -v
	@echo "✅ All tests passed"

coverage:
	@echo "📊 Running tests with coverage..."
	$(PYTEST) tests/unit/ --cov=src/hexawyn --cov-report=term --cov-fail-under=80
	@echo "✅ Coverage threshold met"

update-badge:
	@echo "🏷️  Updating test count badge in README.md..."
	$(PYTHON) scripts/update_test_badge.py
	@echo "✅ Badge updated"

# ─────────────────────────────────────
#  k3d E2E Cluster
# ─────────────────────────────────────

.PHONY: cluster-up cluster-down cluster-load cluster-reset cluster-status cluster-otel cluster-operators

CLUSTER_NAME := hexawyn-e2e

cluster-up:
	@echo "🚀 Creating k3d test cluster..."
	@which k3d > /dev/null 2>&1 || ( \
		echo "❌ k3d not found. Install:"; \
		echo "   curl -s https://raw.githubusercontent.com/k3d-io/k3d/main/install.sh | bash"; \
		exit 1)
	@which docker > /dev/null 2>&1 || ( \
		echo "❌ Docker not found. Install Docker Desktop."; \
		exit 1)
	@if k3d cluster list --no-headers 2>/dev/null | grep -q $(CLUSTER_NAME); then \
		echo "✅ Cluster '$(CLUSTER_NAME)' already exists."; \
	else \
		k3d cluster create $(CLUSTER_NAME) \
			--agents 1 \
			--wait \
			--timeout 120s \
			--k3s-arg "--disable=traefik@server:0" \
			--k3s-arg "--disable=servicelb@server:0"; \
	fi
	@k3d kubeconfig merge $(CLUSTER_NAME) -d ~/.kube/config -s $(CLUSTER_NAME) 2>/dev/null || true
	@kubectl --context k3d-$(CLUSTER_NAME) create namespace hexawyn-test --dry-run=client -o yaml | kubectl --context k3d-$(CLUSTER_NAME) apply -f -
	@echo "✅ Cluster ready (context: k3d-$(CLUSTER_NAME))"
	@echo "   Run: make cluster-load && make test-e2e"

cluster-down:
	@echo "🗑️  Deleting k3d test cluster..."
	-k3d cluster delete $(CLUSTER_NAME)
	@rm -f /tmp/k3d-$(CLUSTER_NAME).yaml
	@echo "✅ Cluster deleted"

cluster-reset:
	@$(MAKE) cluster-down || true
	@$(MAKE) cluster-up

cluster-status:
	@k3d cluster list
	@echo ""
	@kubectl get nodes 2>/dev/null || echo "No cluster running"

cluster-load: cluster-operators cluster-otel
	@echo "📦 Creating namespace and loading E2E fixtures..."
	@k3d kubeconfig get $(CLUSTER_NAME) > /tmp/k3d-$(CLUSTER_NAME).yaml 2>/dev/null || true
	kubectl --kubeconfig=/tmp/k3d-$(CLUSTER_NAME).yaml create namespace hexawyn-test --dry-run=client -o yaml | kubectl --kubeconfig=/tmp/k3d-$(CLUSTER_NAME).yaml apply -f -
	kubectl --kubeconfig=/tmp/k3d-$(CLUSTER_NAME).yaml apply -f tests/e2e/fixtures/ -n hexawyn-test
	@echo "✅ Fixtures loaded"

cluster-otel:
	@echo "📦 Installing Jaeger + Prometheus + Hotrod..."
	@k3d kubeconfig get $(CLUSTER_NAME) > /tmp/k3d-$(CLUSTER_NAME).yaml 2>/dev/null || true
	kubectl --kubeconfig=/tmp/k3d-$(CLUSTER_NAME).yaml create namespace observability --dry-run=client -o yaml | kubectl --kubeconfig=/tmp/k3d-$(CLUSTER_NAME).yaml apply -f -
	kubectl --kubeconfig=/tmp/k3d-$(CLUSTER_NAME).yaml apply -f tests/e2e/fixtures/otel/jaeger.yaml
	kubectl --kubeconfig=/tmp/k3d-$(CLUSTER_NAME).yaml apply -f tests/e2e/fixtures/otel/prometheus.yaml
	@echo "⏳ Waiting for Jaeger + Prometheus to be available..."
	kubectl --kubeconfig=/tmp/k3d-$(CLUSTER_NAME).yaml wait --for=condition=Available --timeout=120s \
		-n observability deployment/jaeger-all-in-one deployment/prometheus
	@echo "✅ OTEL stack ready"

cluster-operators:
	@echo "📦 Installing cert-manager + Tekton + KEDA + ArgoCD..."
	@k3d kubeconfig get $(CLUSTER_NAME) > /tmp/k3d-$(CLUSTER_NAME).yaml 2>/dev/null || true
	kubectl --kubeconfig=/tmp/k3d-$(CLUSTER_NAME).yaml apply --server-side --force-conflicts -f https://github.com/cert-manager/cert-manager/releases/download/v1.14.5/cert-manager.yaml
	kubectl --kubeconfig=/tmp/k3d-$(CLUSTER_NAME).yaml apply --server-side --force-conflicts -f https://storage.googleapis.com/tekton-releases/pipeline/latest/release.yaml
	kubectl --kubeconfig=/tmp/k3d-$(CLUSTER_NAME).yaml apply --server-side --force-conflicts -f https://github.com/kedacore/keda/releases/download/v2.14.0/keda-2.14.0.yaml
	@echo "⏳ Waiting for operator CRDs to be established..."
	kubectl --kubeconfig=/tmp/k3d-$(CLUSTER_NAME).yaml wait --for=condition=Established --timeout=120s \
		crd/issuers.cert-manager.io crd/certificates.cert-manager.io \
		crd/scaledobjects.keda.sh crd/pipelineruns.tekton.dev
	@echo "⏳ Waiting for admission webhooks to be available..."
	kubectl --kubeconfig=/tmp/k3d-$(CLUSTER_NAME).yaml wait --for=condition=Available --timeout=180s \
		-n cert-manager deployment/cert-manager deployment/cert-manager-cainjector deployment/cert-manager-webhook
	kubectl --kubeconfig=/tmp/k3d-$(CLUSTER_NAME).yaml wait --for=condition=Available --timeout=180s \
		-n tekton-pipelines deployment/tekton-pipelines-webhook
	@echo "✅ Operators installed"

# ─────────────────────────────────────
#  Docker
# ─────────────────────────────────────

.PHONY: build run-mcp run-cli run-demo run-cli-demo stop mcp-inspector

version:
	@echo "📦 hexawyn version:"
	$(POETRY) run hexa version

mcp-inspector:  ## Open MCP Inspector UI to browse/test the hexawyn MCP tools
	@echo "🔍 Launching MCP Inspector (http://localhost:6274)..."
	@echo "   Browse the registered MCP tools and test them live."
	@echo "   Ctrl+C to stop."
	@npx -y @modelcontextprotocol/inspector -- poetry run python -m hexawyn.mcp.stdio

build:
	@echo "🐳 Building Docker image..."
	docker build -t $(DOCKER_IMAGE) .
	@echo "✅ Image built: $(DOCKER_IMAGE)"

run-mcp:
	@echo "🚀 Starting MCP server (real cluster)..."
	docker compose -f docker/docker-compose.yml up hexawyn

run-cli:
	@echo "🖥️  Starting CLI Textual against your kubeconfig..."
	HEXAWYN_DISABLE_ENCRYPTION=true HEXAWYN_DEMO_MODE=false $(POETRY) run hexa start

run-demo:
	@echo "🎭 Starting MCP server in demo mode (no cluster)..."
	docker compose -f docker/docker-compose.yml up hexawyn-demo

run-cli-demo:
	@echo "🎭 Starting CLI in demo mode (no cluster)..."
	HEXAWYN_DISABLE_ENCRYPTION=true HEXAWYN_DEMO_MODE=true $(POETRY) run hexa start

# ── Demo — per provider ──────────────────────────────────

.PHONY: run-demo-aws run-demo-azure run-demo-gcp run-demo-openshift run-demo-datadog run-demo-docker

run-demo-aws:  ## Start CLI in AWS EKS demo mode
	HEXAWYN_DISABLE_ENCRYPTION=true HEXAWYN_DEMO_MODE=true HEXAWYN_DEMO_SCENARIO=aws_eks $(POETRY) run hexa start

run-demo-azure:  ## Start CLI in Azure AKS demo mode
	HEXAWYN_DISABLE_ENCRYPTION=true HEXAWYN_DEMO_MODE=true HEXAWYN_DEMO_SCENARIO=azure_aks $(POETRY) run hexa start

run-demo-gcp:  ## Start CLI in GCP GKE demo mode
	HEXAWYN_DISABLE_ENCRYPTION=true HEXAWYN_DEMO_MODE=true HEXAWYN_DEMO_SCENARIO=gcp_gke $(POETRY) run hexa start

run-demo-openshift:  ## Start CLI in OpenShift demo mode
	HEXAWYN_DISABLE_ENCRYPTION=true HEXAWYN_DEMO_MODE=true HEXAWYN_DEMO_SCENARIO=openshift $(POETRY) run hexa start

run-demo-datadog:  ## Start CLI in Datadog demo mode
	HEXAWYN_DISABLE_ENCRYPTION=true HEXAWYN_DEMO_MODE=true HEXAWYN_DEMO_SCENARIO=datadog $(POETRY) run hexa start

run-demo-docker:  ## Start MCP server in Docker demo mode (aws_eks)
	docker run \
		-e ANTHROPIC_API_KEY=$(ANTHROPIC_API_KEY) \
		-e HEXAWYN_DISABLE_ENCRYPTION=true \
		-e HEXAWYN_DEMO_MODE=true \
		-e HEXAWYN_DEMO_SCENARIO=aws_eks \
		-p 8000:8000 \
		hexawyn

stop:
	@echo "🛑 Stopping all Docker services..."
	docker compose -f docker/docker-compose.yml down
	@echo "✅ All services stopped"


.PHONY: gate
gate:
	$(POETRY) run python evals/gate.py

# ─────────────────────────────────────
#  Slack
# ─────────────────────────────────────

.PHONY: slack-listen slack-listen-http

slack-listen:
	@echo "🔌 Starting Slack Socket Mode listener (no public URL needed)..."
	$(POETRY) run hexa slack listen

slack-listen-http:
	@echo "🔌 Starting Slack HTTP Events API listener (requires public URL)..."
	$(POETRY) run hexa slack listen --http

# ─────────────────────────────────────
#  Guard
# ─────────────────────────────────────

.PHONY: guard

guard:
	@echo "🛡️  Running hexa_guard..."
	$(PYTHON) hexa_guard.py
	@echo "✅ Guard rules validated"

# ─────────────────────────────────────
#  DuckDB
# ─────────────────────────────────────

.PHONY: db-size db-purge db-purge-dry db-purge-old db-clean

db-size:
	@echo "📊 DuckDB file size..."
	@$(POETRY) run hexa db size

db-purge:
	@echo "🧹 Purging expired incidents..."
	@$(POETRY) run hexa db purge

db-purge-dry:
	@echo "🔍 Dry run — preview expired incidents to delete..."
	@$(POETRY) run hexa db purge --dry-run

db-purge-old:
	@echo "🧹 Purging incidents older than $(DAYS) days..."
	@$(POETRY) run hexa db purge --older-than $(if $(DAYS),$(DAYS),90)

db-clean:
	@echo "💣 Deleting DuckDB database..."
	@rm -f ~/.hexawyn/memory.duckdb ~/.hexawyn/memory.duckdb.enc
	@echo "✅ DuckDB database deleted"

.PHONY: clean

clean:
	@echo "🧹 Cleaning build artifacts..."
	rm -rf dist/ .coverage coverage.xml htmlcov/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type d -name .pytest_cache -exec rm -rf {} +
	@echo "✅ Clean complete"

# ─────────────────────────────────────
#  Help
# ─────────────────────────────────────

.PHONY: help

help:
	@echo ""
	@echo "══════════════════════════════════════════"
	@echo "     🧠 HEXAWYN — AI Kubernetes Assistant"
	@echo "══════════════════════════════════════════"
	@echo ""
	@echo "📦 DEV SETUP"
	@echo "  make install               → Install Poetry dependencies"
	@echo ""
	@echo "🧪 CODE QUALITY"
	@echo "  make lint                  → Lint Python with ruff"
	@echo "  make format                → Auto-format Python with ruff"
	@echo "  make format-check          → Check formatting with ruff"
	@echo "  make type-check            → Strict mypy type check"
	@echo "  make check                 → Run lint + format-check + type-check"
	@echo "  make guard                 → Run hexa_guard.py rules"
	@echo ""
	@echo "🧪 TESTS"
	@echo "  make test                  → Run unit tests"
	@echo "  make test-integration      → Run integration tests (real DuckDB)"
	@echo "  make test-e2e              → Run E2E tests (requires: make cluster-up)"
	@echo "  make test-all              → Run unit + integration tests"
	@echo "  make coverage              → Run tests with coverage (≥80%)"
	@echo "  make update-badge          → Update test count badge in README.md"
	@echo ""
	@echo "🚀 K3D CLUSTER (E2E)"
	@echo "  make cluster-up            → Create k3d test cluster"
	@echo "  make cluster-down          → Delete k3d test cluster"
	@echo "  make cluster-load          → Load E2E fixtures into cluster"
	@echo "  make cluster-reset         → Delete and recreate cluster"
	@echo "  make cluster-status        → Show cluster status"
	@echo "  make test-e2e-ci           → Full cycle: up + load + test + down"
	@echo ""
	@echo "🐳 DOCKER"
	@echo "  make build                 → Build Docker image"
	@echo "  make run-mcp               → Start MCP server (real cluster)"
	@echo "  make run-demo-docker       → Start MCP server in Docker demo"
	@echo "  make stop                  → Stop all Docker services"
	@echo ""
	@echo "🎭 DEMO"
	@echo "  make run-demo              → Start MCP server in demo mode (compose)"
	@echo "  make run-cli               → Start CLI Textual (real cluster)"
	@echo "  make run-cli-demo          → Start CLI in demo mode"
	@echo "  make gate                  → Run eval gate (deterministic + judge)"
	@echo "  make run-demo-aws          → Start CLI in AWS EKS demo"
	@echo "  make run-demo-azure        → Start CLI in Azure AKS demo"
	@echo "  make run-demo-gcp          → Start CLI in GCP GKE demo"
	@echo "  make run-demo-openshift    → Start CLI in OpenShift demo"
	@echo "  make run-demo-datadog      → Start CLI in Datadog demo"
	@echo ""
	@echo "💬 SLACK"
	@echo "  make slack-listen           → Start Slack Socket Mode listener (local, no VPS)"
	@echo "  make slack-listen-http      → Start Slack HTTP Events API listener (needs public URL)"
	@echo ""
	@echo "🧹 MAINTENANCE"
	@echo "  make clean                 → Remove build artifacts and caches"
	@echo ""
	@echo "🗄️  DUCKDB"
	@echo "  make db-size               → Show DuckDB file size"
	@echo "  make db-purge              → Purge expired incidents"
	@echo "  make db-purge-dry          → Preview what would be purged (dry run)"
	@echo "  make db-purge-old DAYS=90  → Purge older than N days (default 90)"
	@echo "  make db-clean              → Delete DuckDB file entirely"
	@echo ""
	@echo "══════════════════════════════════════════"
	@echo ""
