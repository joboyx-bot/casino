import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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
    WIN_PROBABILITY_C1 = 1 / 6
    WIN_PROBABILITY_C2 = 1 / 6
    C1_wins = 0
    C2_wins = 0
    
    for _ in range(3):
        roll = np.random.rand()
        if roll < WIN_PROBABILITY_C1:
            C1_wins += 1
        elif WIN_PROBABILITY_C1 <= roll < WIN_PROBABILITY_C1 + WIN_PROBABILITY_C2:
            C2_wins += 1
    
    if C1_wins == 0 and C2_wins == 0:
        return '0 wins'
    elif (C1_wins > 0 and C2_wins == 0) or (C2_wins > 0 and C1_wins == 0):
        if max(C1_wins, C2_wins) == 1:
            return '1 win'
        elif max(C1_wins, C2_wins) == 2:
            return '2 wins'
        elif max(C1_wins, C2_wins) == 3:
            return '3 wins'
    elif C1_wins > 0 and C2_wins > 0:
        if C1_wins == 1 and C2_wins == 1:
            return 'both different dice'
        elif (C1_wins == 2 and C2_wins == 1) or (C1_wins == 1 and C2_wins == 2):
            return 'both one two'
    
    print("!!!!! ERROR SHOOULD NOT HAPPEN !!!!!")
    return '0 wins'  # Fallback case

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
num_games = 100
initial_bet = 5
initial_capital = 20000

# Run simulations for each strategy with updated parameters
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
