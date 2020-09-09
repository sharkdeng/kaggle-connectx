
# version 1: # This agent random chooses a non-empty column.
import random

def my_agent(obs, config):
    return random.choice([c for c in range(config.columns) if obs.board[c] == 0])
