import numpy as np
import pandas as pd

# Number of simulations and games
NUM_SIMULATIONS = 100
TOTAL_GAMES = 1440
LOSS_PROBABILITY = 1 / 2 # 0.50

# Function to simulate a single game sequence
def simulate_game_sequence(total_games, loss_probability):
    """
    Simulates a sequence of games, returning a boolean array where True represents a loss and False represents a win.
    
    Args:
    total_games (int): The number of games to simulate.
    loss_probability (float): The probability of losing a single game.
    
    Returns:
    np.array: A 1-dimensional array of booleans representing the game outcomes.
    """
    rand = np.random.rand(total_games)
    # print(rand)
    return rand < loss_probability

# Function to count consecutive losses in a sequence
def count_consecutive_losses(sequence, num_losses):
    """
    Counts the number of times a specific number of consecutive losses occurs in a game sequence.
    
    Args:
    sequence (np.array): The array of game outcomes (True for loss, False for win).
    num_losses (int): The number of consecutive losses to count.
    
    Returns:
    int: The count of consecutive loss streaks.
    """
    max_streak = 0
    current_streak = 0
    for loss in sequence:
        if loss:
            current_streak += 1
            if current_streak >= num_losses:
                max_streak += 1
        else:
            current_streak = 0
    return max_streak

# Run simulations and count streaks
simulation_results = []
for _ in range(NUM_SIMULATIONS):
    game_sequence = simulate_game_sequence(TOTAL_GAMES, LOSS_PROBABILITY)
    # print(game_sequence)
    streaks = {n: count_consecutive_losses(game_sequence, n) for n in range(1, 16)}
    simulation_results.append(streaks)

# Convert results to DataFrame
df_simulations = pd.DataFrame(simulation_results)
print(df_simulations.to_string())
print(df_simulations.describe())
df_probability_loss = df_simulations / TOTAL_GAMES
print(df_probability_loss.to_string())
print(df_probability_loss.describe())

print("-----------------")

# print(np.random.rand(10))
# print(np.random.rand(10) < LOSS_PROBABILITY)