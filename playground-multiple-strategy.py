import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Probabilities based on the game rules
probabilities = {
    '0 wins': 0.5788,  # Updated to sum to 1
    '1 win': 0.3472,
    '2 wins': 0.0694,
    '3 wins': 0.0046
}

# Ensure probabilities sum to 1
assert sum(probabilities.values()) == 1.0, "Probabilities do not sum to 1"

# Payouts based on the game rules
payouts = {
    '0 wins': -1,  # lose the bet
    '1 wins': 2,   # 2x the bet
    '2 wins': 3,  # 3x the bet
    '3 wins': 4   # 4x the bet
}

# Simulate a single game outcome
# def simulate_game():
#     outcome = np.random.choice(['0 wins', '1 win', '2 wins', '3 wins'], p=list(probabilities.values()))
#     return outcome
def simulate_game():
    WIN_PROBABILITY = 1 / 6
    num_wins = 0
    for _ in range(3):
        if np.random.rand() < WIN_PROBABILITY:
            num_wins += 1
    return f"{num_wins} wins"


# Strategy: Flat Betting
def flat_betting(initial_bet, num_games, initial_capital):
    bet = initial_bet
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
    bet = initial_bet
    capital = initial_capital
    for _ in range(num_games):
        if capital <= 0:
            break
        outcome = simulate_game()
        capital -= bet
        capital += bet * payouts[outcome]
        if payouts[outcome] > 0:
            bet = initial_bet
        else:
            bet *= 2
    return capital

def martingale_with_cut_loss(initial_bet, num_games, initial_capital):
    bet = initial_bet
    capital = initial_capital
    consecutive_losses = 0
    
    for _ in range(num_games):
        if capital <= 0:
            break
        outcome = simulate_game()
        capital -= bet
        capital += bet * payouts[outcome]
        
        if payouts[outcome] > 0:
            bet = initial_bet
            consecutive_losses = 0
        else:
            consecutive_losses += 1
            if consecutive_losses >= 10:
                bet = initial_bet
                consecutive_losses = 0
            else:
                bet *= 2
    
    return capital

# Strategy: Reverse Martingale
def reverse_martingale(initial_bet, num_games, initial_capital):
    bet = initial_bet
    capital = initial_capital
    for _ in range(num_games):
        if capital <= 0:
            break
        outcome = simulate_game()
        capital -= bet
        capital += bet * payouts[outcome]
        if payouts[outcome] > 0:
            bet *= 2
        else:
            bet = initial_bet
    return capital

# Strategy: D'Alembert System
def d_alembert(initial_bet, num_games, initial_capital):
    bet = initial_bet
    capital = initial_capital
    for _ in range(num_games):
        if capital <= 0:
            break
        outcome = simulate_game()
        capital -= bet
        capital += bet * payouts[outcome]
        if payouts[outcome] > 0:
            bet = max(initial_bet, bet - initial_bet)
        else:
            bet += initial_bet
    return capital

# Number of simulations, initial bet, and initial capital
num_simulations = 10
num_games = 20
initial_bet = 5
initial_capital = 20000

# Run simulations for each strategy
results = {
    'Flat Betting': [],
    'Martingale': [],
    'Martingale with cut loss': [],
    'Reverse Martingale': [],
    'D\'Alembert': []
}

for _ in range(num_simulations):
    results['Flat Betting'].append(flat_betting(initial_bet, num_games, initial_capital))
    results['Martingale'].append(martingale(initial_bet, num_games, initial_capital))
    results['Martingale with cut loss'].append(martingale_with_cut_loss(initial_bet, num_games, initial_capital))
    results['Reverse Martingale'].append(reverse_martingale(initial_bet, num_games, initial_capital))
    results['D\'Alembert'].append(d_alembert(initial_bet, num_games, initial_capital))

# Convert results to DataFrame
df_results = pd.DataFrame(results)
print(df_results.to_string())

# Display the statistical summary of the results
summary_stats = df_results.describe()
print(summary_stats)
