
# This agent random chooses a non-empty column.
def my_agent(obs, config):
    import random
    return random.choice([c for c in range(config.columns) if obs.board[c] == 0])
