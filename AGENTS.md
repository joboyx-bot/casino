# Repository Guidelines

## Project Structure & Module Organization

This repository is a Python/Poetry workspace for casino and betting-strategy simulations.

| Path | Purpose |
|------|---------|
| `playground.py` | Consecutive-loss probability simulation using NumPy and pandas. |
| `playground-toss-coin*.py` | Coin-toss strategy simulations and probability experiments. |
| `playground-multiple-strategy*.py` | Multiple-strategy simulation variants. |
| `playground-tracker.py` | Tracker-oriented simulation helper script. |
| `consecutive_losses_simulations.csv` | Small checked-in sample/output data. |
| `pyproject.toml` / `poetry.lock` | Poetry dependency and lock files. |
| `setup_env.sh` | Local environment setup helper. |
| `setup_xvfb.sh` | Xvfb setup helper for screenshot/GUI automation needs. |

There is no package module layout yet; scripts are currently run directly from the repository root.

## Build, Test, and Development Commands

Run commands from the repository root.

| Command | Purpose |
|---------|---------|
| `poetry install` | Install Python dependencies from `poetry.lock`. |
| `poetry run python playground.py` | Run the baseline consecutive-loss simulation. |
| `poetry run python playground-toss-coin.py` | Run the main coin-toss strategy comparison. |
| `poetry run python playground-multiple-strategy.py` | Run the main multiple-strategy simulation. |
| `./setup_env.sh` | Create/use the local virtual environment helper flow. |
| `./setup_xvfb.sh` | Prepare Xvfb for scripts that need display/screenshot support. |

No formal test, lint, or format command is currently configured.

## Coding Conventions

- Keep scripts direct and explicit; this repo favors quick simulation experiments over shared abstractions.
- Use NumPy for random simulation and pandas for tabular output, matching the existing scripts.
- Keep simulation constants near the top of each script so scenarios are easy to tune.
- Public helper functions should include docstrings when they are intended to be reused across scripts.

## Testing Guidelines

- There is no isolated automated test suite yet.
- For changes to a simulation script, run that script with `poetry run python <script>.py` and inspect the printed table/summary.
- When adding reusable logic, prefer creating a small focused test setup before expanding script behavior.

## Commit & Workflow Notes

- Existing commits use conventional commit subjects such as `feat: add betting simulation playgrounds`.
- Keep generated local environment folders ignored; `venv` is already ignored.
- `AGENTS.md` is intentionally ignored in this repo per local workspace preference.
