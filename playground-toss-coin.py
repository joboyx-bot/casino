import numpy as np
import pandas as pd

# Simulate a single game outcome for a coin toss
def simulate_game():
    return 'win' if np.random.rand() < 0.5 else 'lose'

# Strategy: Flat Betting
def flat_betting(initial_bet, num_games, initial_capital):
    bet = initial_bet
    capital = initial_capital
    for _ in range(num_games):
        if capital <= 0:
            break
        outcome = simulate_game()
        if outcome == 'win':
            capital += bet
        else:
            capital -= bet
    return capital

# Strategy: Martingale System
def martingale(initial_bet, num_games, initial_capital):
    bet = initial_bet
    capital = initial_capital
    for _ in range(num_games):
        if capital <= 0:
            break
        outcome = simulate_game()
        if outcome == 'win':
            capital += bet
            bet = initial_bet
        else:
            capital -= bet
            bet *= 2
    return capital

# Strategy: Martingale with Cut Loss after 10 Consecutive Losses
def martingale_with_cut_loss(initial_bet, num_games, initial_capital):
    bet = initial_bet
    capital = initial_capital
    consecutive_losses = 0
    for _ in range(num_games):
        if capital <= 0:
            break
        outcome = simulate_game()
        if outcome == 'win':
            capital += bet
            bet = initial_bet
            consecutive_losses = 0
        else:
            capital -= bet
            consecutive_losses += 1
            if consecutive_losses >= 10:
                bet = initial_bet
                consecutive_losses = 0
            else:
                bet *= 2
    return capital

# Strategy: Fibonacci Betting System
def fibonacci_betting(initial_bet, num_games, initial_capital):
    fibonacci_sequence = [1, 1]
    current_bet_index = 0
    capital = initial_capital
    
    for _ in range(num_games):
        if capital <= 0:
            break
        bet = initial_bet * fibonacci_sequence[current_bet_index]
        outcome = simulate_game()
        if outcome == 'win':
            capital += bet
            current_bet_index = 0
        else:
            capital -= bet
            current_bet_index += 1
            if current_bet_index >= len(fibonacci_sequence):
                fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    
    return capital

# Strategy: Oscar's Grind
def oscars_grind(initial_bet, num_games, initial_capital):
    bet = initial_bet
    capital = initial_capital
    win_streak = 0
    
    for _ in range(num_games):
        if capital <= 0:
            break
        outcome = simulate_game()
        if outcome == 'win':
            capital += bet
            win_streak += 1
            bet = initial_bet * (win_streak + 1)
        else:
            capital -= bet
            win_streak = 0
            bet = initial_bet
    
    return capital

# Strategy: Labouchere System
def labouchere_system(initial_bet, num_games, initial_capital):
    sequence = [1, 2, 3, 4]
    capital = initial_capital
    
    for _ in range(num_games):
        if capital <= 0 or len(sequence) == 0:
            break
        bet = initial_bet * (sequence[0] + sequence[-1])
        outcome = simulate_game()
        if outcome == 'win':
            capital += bet
            sequence = sequence[1:-1]
        else:
            capital -= bet
            sequence.append(sequence[0] + sequence[-1])
    
    return capital

# Number of simulations, initial bet, and initial capital
num_simulations = 10
num_games = 1000
initial_bet = 5
initial_capital = 10000

# Run simulations for each strategy with updated parameters
results = {
    'Flat Betting': [],
    'Martingale': [],
    'Martingale with Cut Loss': [],
    'Fibonacci Betting': [],
    'Oscar\'s Grind': [],
    'Labouchere System': []
}

for _ in range(num_simulations):
    results['Flat Betting'].append(flat_betting(initial_bet, num_games, initial_capital))
    results['Martingale'].append(martingale(initial_bet, num_games, initial_capital))
    results['Martingale with Cut Loss'].append(martingale_with_cut_loss(initial_bet, num_games, initial_capital))
    results['Fibonacci Betting'].append(fibonacci_betting(initial_bet, num_games, initial_capital))
    results['Oscar\'s Grind'].append(oscars_grind(initial_bet, num_games, initial_capital))
    results['Labouchere System'].append(labouchere_system(initial_bet, num_games, initial_capital))

# Convert results to DataFrame
df_results = pd.DataFrame(results)
print(df_results.to_string())

# Display the statistical summary of the results
summary_stats = df_results.describe()
print(summary_stats)
