from math import inf

def Minimax_Decision(state):
    best_action, best_val = None, - inf
    for a in actions(state):
        s_prime = result(a, state)
        a_val = Min_Value(s_prime)
        if a_val > best_val:
            best_action = a_val
            best_action = a
    return best_action


def Max_Value(state):
    # Base Case
    if isTerminal(state):
        return utility(state)
    v = - inf
    for a, s in successors(state):
        v = max(v, Min_Value(s))
    return v


def Min_Value(state):
    if isTerminal(state):
        return utility(state)

    v = math.inf
    for a, s in successors(state):
        v = min(v, Max_value(s))
    return v


# Minimax_Decision, Max_Value, Min_Value from CS 3600 class's lecture on Jan. 29th