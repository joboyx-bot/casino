import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Updated probabilities when betting on two colors
probabilities_two_colors = {
    '0 wins': 0.2963,  # None of the chosen colors appear
    '1 win': 0.5926,  # Only one of the chosen colors appears on one die
    '2 wins': 0.2963,  # Only one of the chosen colors appears on two dice
    '3 wins': 0.0741,  # Only one of the chosen colors appears on three dice
    'both different dice': 0.2963,  # Both chosen colors appear on different dice
    'both one two': 0.1481  # One color appears on two dice and the other color appears on one die
}

# Normalize probabilities to ensure they sum to 1
total_probability = sum(probabilities_two_colors.values())
probabilities_two_colors = {k: v / total_probability for k, v in probabilities_two_colors.items()}

# Ensure probabilities sum to 1
assert np.isclose(sum(probabilities_two_colors.values()), 1.0), "Probabilities do not sum to 1"

# Payouts based on the game rules
payouts = {
    '0 wins': -(0.5 * 1) + -(0.5 * 1),
    '1 win': (0.5 * 2) + (0.5 * 0),
    '2 wins': (0.5 * 3) + (0.5 * 0),
    '3 wins': (0.5 * 4) + (0.5 * 0),
    'both different dice': (0.5 * 2) + (0.5 * 2),
    'both one two': (0.5 * 3) + (0.5 * 2)
}

# Simulate a single game outcome
def simulate_game():
    outcome = np.random.choice(list(probabilities_two_colors.keys()), p=list(probabilities_two_colors.values()))
    return outcome

# Strategy: Flat Betting
def flat_betting(initial_bet, num_games, initial_capital):
    bet = initial_bet * 2  # Adjusted for two colors
    capital = initial_capital
    for _ in range(num_games):
        if capital <= 0:
            break
        outcome = simulate_game()
        capital -= bet
        capital += bet * payouts[outcome]
    return capital

# Strategy: Martingale System
def martingale(initial_bet, num_games, initial_capital):
    bet = initial_bet * 2  # Adjusted for two colors
    capital = initial_capital
    for _ in range(num_games):
        if capital <= 0:
            break
        outcome = simulate_game()
        capital -= bet
        capital += bet * payouts[outcome]
        if payouts[outcome] > 0:
            bet = initial_bet * 2  # Adjusted for two colors
        else:
            bet *= 2
    return capital

# Strategy: Martingale with Cut Loss after 10 Consecutive Losses
def martingale_with_cut_loss(initial_bet, num_games, initial_capital):
    bet = initial_bet * 2  # Adjusted for two colors
    capital = initial_capital
    consecutive_losses = 0
    
    for _ in range(num_games):
        if capital <= 0:
            break
        outcome = simulate_game()
        capital -= bet
        capital += bet * payouts[outcome]
        
        if payouts[outcome] > 0:
            bet = initial_bet * 2  # Adjusted for two colors
            consecutive_losses = 0
        else:
            consecutive_losses += 1
            if consecutive_losses >= 10:
                bet = initial_bet * 2  # Adjusted for two colors
                consecutive_losses = 0
            else:
                bet *= 2
    
    return capital

# Number of simulations, initial bet, and initial capital
num_simulations = 10
num_games = 1000
initial_bet = 5
initial_capital = 20000

# Run simulations for each strategy
results = {
    'Flat Betting': [],
    'Martingale': [],
    'Martingale with Cut Loss': []
}

for _ in range(num_simulations):
    results['Flat Betting'].append(flat_betting(initial_bet, num_games, initial_capital))
    results['Martingale'].append(martingale(initial_bet, num_games, initial_capital))
    results['Martingale with Cut Loss'].append(martingale_with_cut_loss(initial_bet, num_games, initial_capital))

# Convert results to DataFrame
df_results = pd.DataFrame(results)
print(df_results.to_string())

# Display the statistical summary of the results
summary_stats = df_results.describe()
print(summary_stats)
