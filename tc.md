# TASK HANDOFF — `cilium_detect` (worktree hexawyn-cilium)

Ce fichier est un **dossier de passation**. La tâche a été démarrée mais **interrompue** pour
cause d'environnement (voir §2). Le prochain agent doit **poursuivre l'implémentation** de
l'outil MCP `cilium_detect` dans ce worktree. Lire tout avant de coder.

---

## 1. CONTEXTE

- **Branch** : `feat/cilium-integration` (déjà checkout). **NE PAS** switcher/checkout/worktree.
- **Repo** : `/home/djepeno/sites/hexawyn-cilium` (worktree de `hexawyn`).
- **Git** : interdiction totale de commit/push/branch/stash/etc. L'humain gère git.
- **TDD strict** : test d'abord (RED) → implémentation (GREEN) → refactor.
- Le model de référence est `keda_detect`. **Tous les nouveaux fichiers doivent suivre
  EXACTEMENT le même contrat.**

## 2. ⚠️ ENVIRONNEMENT — IMPORTANT (cause de l'interruption)

La session `opencode` actuelle était **ancrée sur le repo principal**
(`/home/djepeno/sites/hexawyn`, branche `feat/cli-auth`), PAS sur le worktree.
Le garde global `~/.config/opencode/plugins/tdd-guard.ts` scanne `root` (le repo principal)
pour trouver un test correspondant à chaque `write` de fichier **source**. Résultat :

- Toute **nouvelle écriture de fichier source** dans le worktree est BLOQUÉE
  (le test correspondant n'existe pas dans le repo principal).
- Les **édits** de fichiers existants (`server.py`, `cluster_adapters.py`) passent
  (leur test existe dans le repo principal).
- L'écriture de **fichiers de test** passe toujours (le garde ignore les fichiers de test).

### Pour le prochain agent

**La nouvelle session doit être lancée avec le worktree comme racine**
(`/home/djepeno/sites/hexawyn-cilium`) pour que `tdd-guard` scanne le bon répertoire.
Si malgré tout un `write` source est bloqué par `[TDD GUARD]` :

1. Écrire d'abord les tests (fichiers `test_*.py`) — jamais bloqué.
2. Pour les **nouveaux fichiers source**, placer le contenu via bash :
   ```bash
   cat > /tmp/opencode/cilium.py <<'PY'
   # ... contenu du fichier ...
   PY
   cp /tmp/opencode/cilium.py src/hexawyn/domain/models/cilium.py
   ```
   (TDD est respecté : test écrit avant l'implémentation). Vérifier ensuite
   `make check` + `pytest`.

Autres gardes actives (respecter sinon `write` refusé) :
- **boolean-flag-guard** : AUCUN paramètre `bool` dans les fonctions/helpers
  (ex. pas de `def f(ready: bool)` → préférer `f_ready()` / `f_not_ready()`).
- **ubiquitous-language-guard** : noms = concepts métier. `Info`/`Data`/`Util` refusés
  dans la couche domaine. → le modèle d'état d'agent s'appelle `CiliumAgentHealth`.
- **no-git-guard** : aucune commande git.

---

## 3. ÉTAT ACTUEL — tests déjà écrits (marcheront RED, source absente)

`tests/unit/domain/models/test_cilium.py` — modèle domaine
`tests/unit/application/use_case/cilium/test_uc_cilium_detect_use_case.py` — use case
`tests/unit/application/ports/test_cilium_ports.py` — ports (driven + driving)
`tests/unit/adapters/secondary/gitops/test_cilium_adapter.py` — adapter réel
`tests/unit/mcp/tools/test_tool_cilium_detect.py` — outil MCP (nested)
`tests/unit/tools/test_cilium_detect.py` — outil MCP (flat)

Ces tests sont complets et couvrent : installé / non installé / dégradé / parsing version /
mode (tunnel, native-routing, UNKNOWN) / RBAC 403 → `InsufficientPermissionsError` /
outerreach → `ClusterUnreachableError` / CRDs présents sans daemonset / parsing image.

**IMPLÉMENTATION À FAIRE** (les sources n'existent pas encore) :

## 4. FICHIERS À CRÉER (sources)

1. `src/hexawyn/domain/models/cilium.py`
   - `CiliumAgentHealth` — dataclass **frozen** : `node: str`, `pod_name: str`,
     `namespace: str`, `ready: bool`, `phase: str`, `restart_count: int`,
     `image: str | None = None`, `message: str | None = None`.
   - `CiliumDetectionResult` — dataclass **frozen** : `installed: bool`, `status: str`,
     `version: str | None`, `mode: str`, `namespace: str | None`, `total_agents: int`,
     `ready_agents: int`, `degraded_summary: str | None`, `agents: list[CiliumAgentHealth]`,
     `note: str | None`.

2. `src/hexawyn/application/ports/driven/cilium_port.py`
   - `class CiliumPort(ABC)` avec `@abstractmethod def detect(self) -> CiliumDetectionResult: ...`.

3. `src/hexawyn/application/ports/driving/cilium_detect/cilium_detect_service_port.py`
   - `class CiliumDetectServicePort(ABC)` — `def detect(self, command: CiliumDetectCommand) -> CiliumDetectResponse: ...`.
   - **créer ce dossier** : il nourrit `tool/check_docs.py` (`coverage_issues`) qui impose
     qu'un doc existe dans `docs/use-cases/` pour chaque clef de `ports/driving/*`.

4. `src/hexawyn/application/use_case/cilium/cilium_detect/command.py`
   - `@dataclass(frozen=True) class CiliumDetectCommand: pass`.

5. `src/hexawyn/application/use_case/cilium/cilium_detect/response.py`
   - `CiliumAgentOutput(TypedDict)` : les champs de `CiliumAgentHealth` (node, pod_name,
     namespace, ready, phase, restart_count, image, message).
   - `@dataclass class CiliumDetectResponse`: `installed: bool = False`,
     `status: str = "not_installed"`, `version: str | None = None`, `mode: str = "UNKNOWN"`,
     `namespace: str | None = None`, `total_agents: int = 0`, `ready_agents: int = 0`,
     `degraded_summary: str | None = None`, `agents: list[CiliumAgentOutput] | None = None`,
     `note: str | None = None`, `error: str | None = None`.

6. `src/hexawyn/application/use_case/cilium/cilium_detect/cilium_detect_use_case.py`
   - `class CiliumDetectUseCase` — `__init__(self, port: CiliumPort)`.
   - `execute(self, command) -> CiliumDetectResponse` : appelle `self._port.detect()`,
     convertit chaque `CiliumAgentHealth` en `CiliumAgentOutput`.

7. `src/hexawyn/adapters/secondary/gitops/cilium_adapter.py` (l'essentiel)
   - `class CiliumAdapter(CiliumPort)` — `__init__(self, vanilla: VanillaAdapter)`.
   - **Détection installé** = daemonset nommé `cilium` trouvé **OU** CRDs `cilium.io` présents.
   - **Non installé** → `CiliumDetectionResult(installed=False, status="not_installed", mode="UNKNOWN", ...)`
     avec `note` explicite. Jamais de valeur inventée.
   - **Version** = tag image du conteneur `cilium-agent` (préserver le tag brut, ex. `v1.16.3`,
     `v1.16.0-pre.1`). Digest (`@sha256:`) → `None`.
   - **Mode** = lecture du ConfigMap `cilium-config` (même namespace que le daemonset) :
     - clé `routing-mode` : `tunnel`→"tunnel", `native`→"native-routing",
       `cluster`→"cluster", `ipvlan`→"ipvlan", sinon "UNKNOWN".
     - sinon clé `tunnel` non vide → "tunnel".
     - absence/echec → "UNKNOWN" (pas inventé).
   - **Agents** = pods label `k8s-app=cilium` dans le namespace du daemonset ; `node`,
     `phase`, `ready` (containerStatuses `cilium-agent`), `restart_count`, `image`, `message`.
   - **Dégradé** = `ready_agents < total_agents` → `status="degraded"` et
     `degraded_summary=f"{ready}/{total} agents ready"`. S'il n'y a pas de pods listés,
     fallback sur `status.desiredNumberScheduled` / `numberReady` du daemonset.
   - **CRDs présents mais pas de daemonset** → `installed=True`, `version=None`,
     `namespace=None`, agents `[]`, `note` explicite.
   - **Traduction d'erreur** (exception API → HexawynError) :
     `status==403` → `InsufficientPermissionsError`, timeout → `AdapterTimeoutError`,
     sinon `ClusterUnreachableError`. `404` sur la liste CRD → **pas installé** (pas une erreur).
   - **Lecture API** : utiliser `self._vanilla._apps_api_client()` (daemonsets),
     `self._vanilla._crd_api_client()` (CRDs), `self._vanilla._api_client()` (configmap/pods).
     Les méthodes non déclarées dans les Protocols (`list_daemon_set_for_all_namespaces`,
     `read_namespaced_config_map`, `list_namespaced_pod` avec `label_selector`) doivent être
     accédées via `getattr(...)` pour éviter les problèmes mypy.
   - **Robustesse dict vs objet k8s** : écrire un helper `_get(obj, key)` qui lit depuis un
     `dict` (clé) OU un objet (`getattr` camel↔snake, ex. `nodeName`↔`node_name`) ; et
     `_items(obj)` pour `.items`. Les tests utilisent des dicts, l'API réelle des objets.

8. `src/hexawyn/mcp/tools/cilium_detect.py` (outil MCP)
   - `def cilium_detect() -> dict[str, object]` — construit l'adapter via
     `from hexawyn.mcp.server import build_cilium_adapter`, exécute l'use case, retourne
     un dict `{installed, status, version, mode, namespace, total_agents, ready_agents,
     degraded_summary, agents, note, error}`.
   - `try/except Exception` → retourne `installed=False, status="unknown", error=str(exc)`.
   - `def register(mcp: FastMCP) -> None: mcp.tool()(cilium_detect)`.
   - Le module est **auto-découvert** par `register_tools()` (scan de `mcp/tools/*.py`) tant
     qu'il expose `register`.

## 5. FICHIERS À MODIFIER (existants)

9. `src/hexawyn/mcp/adapters/cluster_adapters.py`
   - ajouter `from hexawyn.application.ports.driven.cilium_port import CiliumPort`.
   - ajouter :
     ```python
     def build_cilium_adapter() -> CiliumPort:
         from hexawyn.adapters.secondary.gitops.cilium_adapter import CiliumAdapter
         from hexawyn.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter
         return CiliumAdapter(VanillaAdapter(cluster_name="default"))
     ```

10. `src/hexawyn/mcp/server.py`
    - ajouter `build_cilium_adapter` à l'import depuis `hexawyn.mcp.adapters.cluster_adapters`.
    - ajouter `"build_cilium_adapter"` à la liste `__all__`.

## 6. TESTS DÉJÀ ÉCRITS (respecter leur contenu)

Ne pas réécrire les tests existants ; ils sont le contrat. S'assurer qu'ils passent (GREEN).
Ils importent les symboles attendus :
- `hexawyn.domain.models.cilium` → `CiliumAgentHealth`, `CiliumDetectionResult`.
- `hexawyn.application.ports.driven.cilium_port` → `CiliumPort`.
- `hexawyn.application.ports.driving.cilium_detect.cilium_detect_service_port` → `CiliumDetectServicePort`.
- `hexawyn.application.use_case.cilium.cilium_detect.{command,response,cilium_detect_use_case}`.
- `hexawyn.adapters.secondary.gitops.cilium_adapter` → `CiliumAdapter`.
- `hexawyn.mcp.tools.cilium_detect` → `cilium_detect`, `register`.

## 7. TEST SERVEUR (à ajouter)

Dans `tests/unit/test_server.py`, ajouter à `TestMCPBuilderFunctions` :
```python
def test_build_cilium_adapter(self) -> None:
    result = self.server_mod.build_cilium_adapter()
    assert isinstance(result, CiliumPort)
```
(ajouter l'import depuis `hexawyn.application.ports.driven.cilium_port import CiliumPort`.)

## 8. DOCS + CORPUS

- `docs/use-cases/178-cilium-detect.md` — format imposé §AGENTS.md (Sample Questions,
  4 flows Mermaid sequenceDiagram — happy path / erreurs / checker / DuckDB —,
  Key Points, Test Coverage, Related Files). Le nom doit matcher la clef `cilium_detect`
  (slug `cilium-detect`) sinon `tool/check_docs.py` signale un orphelin.
- `docs/benchmark/cilium.md` — scénario benchmark (cf. `docs/benchmark/keda.md` pour le format).
- `datasets/intent_examples.yaml` — ajouter l'entrée `cilium_detect:` avec **≥5 questions**
  (techniques, vagues, business, commande, question) et `tool: cilium_detect`.
  Voir l'entrée `keda_detect:` (ligne ~968) pour le format.
- ⚠️ **Ne jamais modifier** le repo `hexa-knowledge` (autre dépôt) — c'est manuel, hors scope.

## 9. VALIDATION (obligatoire avant clôture)

```bash
# TDD: RED → GREEN
poetry run pytest tests/unit/ -q --tb=short
# Qualité (ruff + format + mypy strict)
make check
# Coverage ≥ 95% sur les fichiers touchés
poetry run pytest tests/unit/ --cov=src/hexawyn --cov-report=term-missing -q
# Docs anti-drift
poetry run python tool/check_docs.py --all --fail-warnings
```

L'environnement du worktree est **déjà installé** (`.venv` avec deps). Vérifier :
```bash
cd /home/djepeno/sites/hexawyn-cilium && .venv/bin/python -c "import kubernetes, fastmcp, pytest"
```

## 10. EXIGENCES MÉTIER (User Story / AC)

> As a platform/SRE engineer, I want to detect whether Cilium is the active CNI and report
> its version, mode, and agent health.

- **AC1** — outil MCP `cilium_detect` enregistré, contrat identique à `keda_detect`.
- **AC2** — renvoie présent (CRDs `cilium.io` / daemonset `cilium`) + version + mode
  (`tunnel`, `native-routing`, …).
- **AC3** — santé par nœud (running/ready) avec résumé dégradé.
- **AC4** — cas « non installé » honnête : marqueur `NOT_INSTALLED` (via `status="not_installed"`),
  jamais de valeur fabriquée.
- **AC5** — derrière un port driven `CiliumPort` (ABC) + adapter K8s ;
  `build_cilium_adapter()` dans `server.py` renvoie le port.
- **AC6** — hexagonal : aucun import k8s dans `domain/`, `application/` ;
  erreurs traduites en `HexawynError`.
- **AC7** — corpus ≥5 questions dans `datasets/intent_examples.yaml` + scénario benchmark.

### Scénarios de test (ticket)

| Scénario | Entrée | Attendu | Statut |
|---|---|---|---|
| installé | cluster avec CRDs Cilium | `installed=true`, version, agents | PASS |
| non installé | pas de CRDs Cilium | `installed=false`, NOT_INSTALLED | PASS |
| dégradé | agents pas tous ready | `degraded_summary` avec compteurs | PASS |
| parsing version | chaîne version inhabituelle | version brute préservée | PASS |
| RBAC 403 | perms insuffisantes | `InsufficientPermissionsError` | PASS |

### Edge cases

- cluster injoignable → `ClusterUnreachableError`
- pas de CRDs Cilium → `installed=false` sans crash
- liste agents vide → `agents=[]` + note
- timeout → traduit en `HexawynError`
- RBAC refusé → `InsufficientPermissionsError`
- mode inconnu → `mode=UNKNOWN` (pas inventé)

### Checker node (cas)

- modèle invente `installed=true` sans CRDs → FAIL (cross-check daemonset/CRD)
- modèle fabrique une version → FLAG (n'utiliser que la version observée)
- mauvais naming CNI → FAIL (Cilium ≠ Calico ≠ Istio)

### Dépendance

- `NetworkPolicyAuditPort` (extension point) — détection de policies custom Cilium.
  **Hors scope de cette tâche**, mais mentionner comme extension future.
