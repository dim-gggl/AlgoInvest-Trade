import itertools


def brute_force(actions: list, budget: float) -> tuple:
    """
    Finds the most profitable combination of actions 
    within a given budget.
    Args:
        actions (list): List of actions, each with cost 
                        and profit attributes.
        budget (float): Maximum allowable budget.
    Returns:
        tuple: Best combination's total cost, list of 
               actions, and total profit.
    """
    best_cost = 0
    best_combination = None
    best_profit = 0
    # Iterate over all possible combination sizes (from 1 to 
    # the total number of actions)
    for n in range(1, len(actions) + 1):
        # Generate all combinations of actions of size `n`
        for combo in itertools.combinations(actions, n):
            total_cost = sum(action.cost for action in combo)
            # Check if the total cost is within the budget
            if total_cost <= budget:
                total_profit = sum(action.profit_value for action in combo)
                if total_profit > best_profit:
                    best_profit = total_profit
                    best_cost = total_cost
                    best_combination = combo
    return best_cost, best_combination, best_profit
