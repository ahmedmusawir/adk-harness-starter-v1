# CHANGELOG.md — ADK Harness Starter v1

---

## 2026-03-02 — [CC] Claude Code — Pre-Phase-1A Cleanup

### Infrastructure Fixes

- **Updated:** `.env_example` — Changed `GOOGLE_GENAI_USE_VERTEXAI=FALSE` to `GOOGLE_GENAI_USE_VERTEXAI=1`. The old value disabled Vertex AI entirely, which would cause silent auth failures.
- **Updated:** `Dockerfile` — Changed base image from `python:3.11-slim` to `python:3.12-slim`. Aligns with `.python-version` file and project requirements.
- **Updated:** `grant_permissions.sh` — Added `roles/secretmanager.secretAccessor` IAM grant. Without this, Cloud Run crashes at startup when loading secrets via `--set-secrets`.

### Agent Code Fixes

- **Updated:** `ghl_mcp_agent/agent.py` — Fixed stale file header comment (`# /calc_agent/agent.py` → `# ghl_mcp_agent/agent.py`).
- **Updated:** `jarvis_agent/agent.py` — Removed unused `from google import genai` import.

### Git / Security

- **Updated:** `.gitignore` — Added explicit `ghl_mcp_agent/.env` entry to ensure agent-scoped env files are never committed.

### Documentation Fixes

- **Updated:** `docs/NAMING_CONVENTIONS.md` — Updated GCS Paths section to reflect actual bucket path schema used in code (`ADK_Agent_Bundle_1/{agent_name}/` prefix, not the planned `agents/{agent_name}/` prefix).
- **Updated:** `docs/APP_BRIEFS/MASTER_BRIEF_v1.2.md` — Fixed repo name (`adk-harness-modules-workshop-v1` → `adk-harness-starter-v1`). Replaced `shared/` references with `utils/` for token_calculator and run_receipt stubs.
- **Updated:** `docs/APP_BRIEFS/PHASE_1_OVERVIEW.md` — Replaced all `shared/` references with `utils/`, all `token_tracker.py` references with `token_calculator.py`, and repo name. Updated title.
- **Updated:** `docs/APP_BRIEFS/PHASE_1_TESTING_STRATEGY.md` — Replaced all `shared/` references with `utils/`, all `token_tracker` module references with `token_calculator`. Updated title.
- **Updated:** `docs/APP_BRIEFS/STARTER_KIT_SPEC.md` — Fixed repo name in target file structure diagram.
- **Updated:** `docs/APP_BRIEFS/PHASE_1A_AGENT_SET_1_RICO_CACHING.md` — Fixed repo name in both file structure diagrams (lines 42, 383).

### Noted for Future Fix (Not In This Batch)

- `docs/APP_BRIEFS/PHASE_1_TESTING_STRATEGY.md` — Test function names `test_token_tracker_captures_metrics` / `test_token_tracker_fields_are_numeric` still use old module name. Cosmetic only; rename when writing actual tests.
- `deploy.sh` — Missing `--no-cpu-throttling`, `--cpu-boost`, `--min-instances 1` flags required for ADK streaming workloads. Placeholder `GCS_BUCKET_NAME="your-agent-instructions-bucket-name"` not filled in.
- `requirements.txt` — ~134 packages installed, many unused (yfinance, pandas, huggingface-hub, litellm, etc.). Prune before Phase 1A build.
- `docs/APP_BRIEFS/PHASE_1_OVERVIEW.md` + `PHASE_1A` brief — GCS Bucket Structure section still shows planned `agents/{agent}/` paths; actual code uses `ADK_Agent_Bundle_1/` prefix. Architectural decision needed before Phase 1A.

---

*[CC] = Claude Code change | [TS] = Tony Stark manual edit*
