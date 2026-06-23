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

# ─────────────────────────────────────
#  Dev setup
# ─────────────────────────────────────

.PHONY: install

install:
	@echo "📦 Installing all dependencies..."
	$(POETRY) install --with dev
	@echo "✅ Dependencies installed"

# ─────────────────────────────────────
#  Code quality
# ─────────────────────────────────────

.PHONY: lint format type-check check

lint:
	@echo "🔍 Linting Python with ruff..."
	$(RUFF) check src/ tests/
	@echo "✅ Lint passed"

format:
	@echo "🎨 Formatting Python with ruff..."
	$(RUFF) format src/ tests/
	@echo "✅ Formatting done"

type-check:
	@echo "🔎 Running mypy strict type check..."
	$(MYPY) src/hexawyn/
	@echo "✅ Type check passed"

check:
	@echo "🔍 Running all quality checks..."
	@echo ""
	@$(MAKE) lint
	@$(MAKE) type-check
	@echo ""
	@echo "✅ All checks passed"

# ─────────────────────────────────────
#  Tests
# ─────────────────────────────────────

.PHONY: test test-integration test-all coverage

test:
	@echo "🧪 Running unit tests..."
	$(PYTEST) tests/unit/ -v --tb=short
	@echo "✅ Unit tests passed"

test-integration:
	@echo "🔬 Running integration tests (real DuckDB, DemoAdapter)..."
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
	@echo "🖥️  Starting CLI Textual (real cluster)..."
	hexa start

run-demo:
	@echo "🎭 Starting MCP server in demo mode (no cluster)..."
	docker compose -f docker/docker-compose.yml up hexawyn-demo

run-cli-demo:
	@echo "🎭 Starting CLI in demo mode (no cluster)..."
	HEXAWYN_DEMO_MODE=true hexa start

# ── Demo — per provider ──────────────────────────────────

.PHONY: run-demo-aws run-demo-azure run-demo-gcp run-demo-openshift run-demo-datadog run-demo-docker

run-demo-aws:  ## Start CLI in AWS EKS demo mode
	HEXAWYN_DEMO_MODE=true HEXAWYN_DEMO_SCENARIO=aws_eks poetry run hexa start

run-demo-azure:  ## Start CLI in Azure AKS demo mode
	HEXAWYN_DEMO_MODE=true HEXAWYN_DEMO_SCENARIO=azure_aks poetry run hexa start

run-demo-gcp:  ## Start CLI in GCP GKE demo mode
	HEXAWYN_DEMO_MODE=true HEXAWYN_DEMO_SCENARIO=gcp_gke poetry run hexa start

run-demo-openshift:  ## Start CLI in OpenShift demo mode
	HEXAWYN_DEMO_MODE=true HEXAWYN_DEMO_SCENARIO=openshift poetry run hexa start

run-demo-datadog:  ## Start CLI in Datadog demo mode
	HEXAWYN_DEMO_MODE=true HEXAWYN_DEMO_SCENARIO=datadog poetry run hexa start

run-demo-docker:  ## Start MCP server in Docker demo mode (aws_eks)
	docker run \
		-e ANTHROPIC_API_KEY=$(ANTHROPIC_API_KEY) \
		-e HEXAWYN_DEMO_MODE=true \
		-e HEXAWYN_DEMO_SCENARIO=aws_eks \
		-p 8000:8000 \
		hexawyn

stop:
	@echo "🛑 Stopping all Docker services..."
	docker compose -f docker/docker-compose.yml down
	@echo "✅ All services stopped"

# ─────────────────────────────────────
#  Guard
# ─────────────────────────────────────

.PHONY: guard

guard:
	@echo "🛡️  Running hexa_guard..."
	$(PYTHON) hexa_guard.py
	@echo "✅ Guard rules validated"

# ─────────────────────────────────────
#  Clean
# ─────────────────────────────────────

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
	@echo "  make type-check            → Strict mypy type check"
	@echo "  make check                 → Run lint + type-check"
	@echo "  make guard                 → Run hexa_guard.py rules"
	@echo ""
	@echo "🧪 TESTS"
	@echo "  make test                  → Run unit tests"
	@echo "  make test-integration      → Run integration tests (real DuckDB)"
	@echo "  make test-all              → Run unit + integration tests"
	@echo "  make coverage              → Run tests with coverage (≥80%)"
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
	@echo "🧹 MAINTENANCE"
	@echo "  make clean                 → Remove build artifacts and caches"
	@echo ""
	@echo "══════════════════════════════════════════"
	@echo ""
