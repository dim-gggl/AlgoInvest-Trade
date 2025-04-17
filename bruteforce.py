import itertools


def brute_force(actions: list, budget: float) -> tuple:

        """
        Finds the best combination of actions to maximize profit while staying within a given budget.

        Args:
            actions (list): A list of action objects, where each action has `cost` and `profit_value` attributes.
            budget (float): The maximum allowable budget for the selected actions.

        Returns:
            tuple: A tuple containing:
                - best_cost (float): The total cost of the best combination of actions.
                - best_combination (tuple): The combination of actions that yields the highest profit.
                - best_profit (float): The total profit of the best combination of actions.
        """
        best_cost = 0
        best_combination = None
        best_profit = 0
        # We start by checking all sizes of combinations for 1 to all
        for i in range(1, len(actions) + 1):
            # For each combination, we calculate the sum of all actions
            for combo in itertools.combinations(actions, i):
                total_cost = sum(action.cost for action in combo)
                if total_cost <= budget:
                    # If the sum of all combination costs is less than the budget
                    total_profit = sum(action.profit_value for action in combo)
                    # Combination is set as the best
                    if total_profit > best_profit:
                        best_profit = total_profit
                        best_cost = total_cost
                        best_combination = combo
        return best_cost, best_combination, best_profit
