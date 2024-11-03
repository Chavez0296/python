
def alpha_beta_search(gameState):
    """ Return the best move along a branch of the game tree
        using alpha-beta pruning.
    """
    alpha = float("-inf")
    beta = float("inf")
    best_score = float("-inf")
    best_move = None
    
    for a in gameState.actions():
        v = min_value(gameState.result(a), alpha, beta)
        if v > best_score:
            best_score = v
            best_move = a
        alpha = max(alpha, best_score)
        
    return best_move

def min_value(gameState, alpha, beta):
    """ Return the minimum value for the current game state. """
    if gameState.terminal_test():
        return gameState.utility(0)  #player 0 

    v = float("inf")
    for a in gameState.actions():
        v = min(v, max_value(gameState.result(a), alpha, beta))
        if v <= alpha:
            return v  # Prune the branch
        beta = min(beta, v)
        
    return v

def max_value(gameState, alpha, beta):
    """ Return the maximum value for the current game state. """
    if gameState.terminal_test():
        return gameState.utility(0)  # player 0

    v = float("-inf")
    for a in gameState.actions():
        v = max(v, min_value(gameState.result(a), alpha, beta))
        if v >= beta:
            return v  # Prune the branch
        alpha = max(alpha, v)
        
    return v