import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Simulate a single game outcome for a coin toss
def simulate_game():
    return 'win' if np.random.rand() < 0.5 else 'lose'

# Strategy: Flat Betting
def flat_betting(initial_bet, num_games, initial_capital):
    bet = initial_bet
    capital_heads = initial_capital / 2
    capital_tails = initial_capital / 2
    
    for _ in range(num_games):
        if capital_heads <= 0 and capital_tails <= 0:
            break
        outcome_heads = simulate_game()
        outcome_tails = 'lose' if outcome_heads == 'win' else 'win'
        
        if capital_heads > 0:
            if outcome_heads == 'win':
                capital_heads += bet
            else:
                capital_heads -= bet
        
        if capital_tails > 0:
            if outcome_tails == 'win':
                capital_tails += bet
            else:
                capital_tails -= bet
    
    return capital_heads + capital_tails

# Strategy: Martingale System
def martingale(initial_bet, num_games, initial_capital):
    bet_heads = initial_bet
    bet_tails = initial_bet
    capital_heads = initial_capital / 2
    capital_tails = initial_capital / 2
    
    for _ in range(num_games):
        if capital_heads <= 0 and capital_tails <= 0:
            break
        outcome_heads = simulate_game()
        outcome_tails = 'lose' if outcome_heads == 'win' else 'win'
        
        if capital_heads > 0:
            if outcome_heads == 'win':
                capital_heads += bet_heads
                bet_heads = initial_bet
            else:
                capital_heads -= bet_heads
                bet_heads *= 2
        
        if capital_tails > 0:
            if outcome_tails == 'win':
                capital_tails += bet_tails
                bet_tails = initial_bet
            else:
                capital_tails -= bet_tails
                bet_tails *= 2
    
    return capital_heads + capital_tails

# Strategy: Martingale with Cut Loss after 10 Consecutive Losses
def martingale_with_cut_loss(initial_bet, num_games, initial_capital):
    bet_heads = initial_bet
    bet_tails = initial_bet
    capital_heads = initial_capital / 2
    capital_tails = initial_capital / 2
    consecutive_losses_heads = 0
    consecutive_losses_tails = 0
    
    for _ in range(num_games):
        if capital_heads <= 0 and capital_tails <= 0:
            break
        outcome_heads = simulate_game()
        outcome_tails = 'lose' if outcome_heads == 'win' else 'win'
        
        if capital_heads > 0:
            if outcome_heads == 'win':
                capital_heads += bet_heads
                bet_heads = initial_bet
                consecutive_losses_heads = 0
            else:
                capital_heads -= bet_heads
                consecutive_losses_heads += 1
                if consecutive_losses_heads >= 10:
                    bet_heads = initial_bet
                    consecutive_losses_heads = 0
                else:
                    bet_heads *= 2
        
        if capital_tails > 0:
            if outcome_tails == 'win':
                capital_tails += bet_tails
                bet_tails = initial_bet
                consecutive_losses_tails = 0
            else:
                capital_tails -= bet_tails
                consecutive_losses_tails += 1
                if consecutive_losses_tails >= 10:
                    bet_tails = initial_bet
                    consecutive_losses_tails = 0
                else:
                    bet_tails *= 2
    
    return capital_heads + capital_tails

# Number of simulations, initial bet, and initial capital
num_simulations = 100
num_games = 100
initial_bet = 5
initial_capital = 10000

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
