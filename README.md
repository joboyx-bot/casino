# Casino Simulations

Python playgrounds for exploring casino-style betting strategies, coin-toss outcomes, and consecutive-loss probabilities.

## Contents

| File | Purpose |
|------|---------|
| `playground.py` | Simulates repeated games and counts consecutive loss streaks. |
| `playground-toss-coin.py` | Compares common coin-toss betting strategies. |
| `playground-toss-coin-2-bets.py` | Coin-toss strategy variant with two-bet behavior. |
| `playground-toss-coin-probability.py` | Probability-focused coin-toss experiment. |
| `playground-multiple-strategy.py` | Multiple betting-strategy simulation. |
| `playground-multiple-strategy-2-bets.py` | Multiple-strategy variant with two-bet behavior. |
| `playground-multiple-strategy-2-bets-2.py` | Additional two-bet strategy variant. |
| `playground-tracker.py` | Tracker helper for simulation runs. |
| `consecutive_losses_simulations.csv` | Sample/output data for consecutive-loss simulations. |

## Setup

This project uses Poetry.

```bash
poetry install
```

If you prefer the local helper script:

```bash
./setup_env.sh
```

For screenshot or GUI automation dependencies:

```bash
./setup_xvfb.sh
```

## Run

Run scripts directly from the repository root:

```bash
poetry run python playground.py
poetry run python playground-toss-coin.py
poetry run python playground-multiple-strategy.py
```

Most scripts print pandas tables or summaries to stdout.

## Development Notes

- Simulation parameters are defined near the top or bottom of each script.
- Dependencies are managed in `pyproject.toml` and pinned in `poetry.lock`.
- No automated test suite is configured yet; validate changes by running the affected script.
