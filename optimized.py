def optimized(actions: list, budget: float):
    """
    Solve the investment optimization problem
    using dynamic programming.
    Args:
        actions (list): List of action objects.
        budget (float): Maximum budget.
    Returns:
        tuple: (total_cost (float), selected_actions (list),
            total_profit (float)).
    """

    # We start by converting amounts to cents
    # to avoid floating point problems

    n = len(actions)
    B = int(budget * 100)

    # A table to track which actions are
    # included in the optimal solution

    dp = [0] * (B + 1)
    keep = [[False] * (B + 1) for _ in range(n)]
    min_cost = min(
        int(action.cost * 100) for action in actions
        )

    # It starts by scanning all actions and compare
    # their prices and profits.

    for i in range(n):
        cost = int(actions[i].cost * 100)
        profit = actions[i].profit

        # Iterate over the budget from the maximum
        # down to the cost of the current action

        for b in range(B, max(min_cost, cost) - 1, -1):

            # Check if including the current
            # action gives a better profit

            if dp[b - cost] + profit > dp[b]:
                dp[b] = dp[b - cost] + profit
                keep[i][b] = True

    # Start with the full budget and
    # an empty list to fill with selected actions

    b = B
    selected_actions = []

    # Iterate over the actions in reverse order
    # to determine which actions were selected

    for i in range(n - 1, -1, -1):

        # Check if the current action was
        # included in the optimal solution

        if keep[i][b]:
            selected_actions.append(actions[i])

            # reduce the budget

            b -= int(actions[i].cost * 100)

    total_cost = sum(
        action.cost for action in selected_actions
        )
    total_profit = sum(
        action.profit for action in selected_actions
        )

    return total_cost, selected_actions, total_profit
