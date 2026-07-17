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

.PHONY: test test-integration test-all coverage update-badge

test:
	@echo "🧪 Running unit tests..."
	$(PYTEST) tests/unit/ -v --tb=short
	@echo "✅ Unit tests passed"

test-integration:
	@echo "🔬 Running integration tests (real DuckDB, demo adapter)..."
	$(PYTEST) tests/integration/ -v -m integration
	@echo "✅ Integration tests passed"

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
#  Docker
# ─────────────────────────────────────

.PHONY: build run-mcp run-cli run-demo run-cli-demo stop

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
	@echo "  make test-all              → Run unit + integration tests"
	@echo "  make coverage              → Run tests with coverage (≥80%)"
	@echo "  make update-badge          → Update test count badge in README.md"
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
