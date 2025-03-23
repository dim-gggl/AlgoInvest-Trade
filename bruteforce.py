from utils.utils import load_actions
from utils.config import BLD, NO_STL
import itertools


def brute_force(actions, budget):
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
        for i in range(1, len(actions) + 1):
            for combo in itertools.combinations(actions, i):
                total_cost = sum(action.cost for action in combo)
                if total_cost <= budget:
                    total_profit = sum(action.profit_value for action in combo)
                    if total_profit > best_profit:
                        best_profit = total_profit
                        best_cost = total_cost
                        best_combination = combo
        return best_cost, best_combination, best_profit


if __name__ == "__main__":
    budget = 500
    actions = load_actions()

    best_cost, best_combination, best_profit = brute_force(actions=actions, budget=budget)
    total_benef = round(best_profit * 100 / best_cost, 2)
    print("Best possible combination :")
    for action in best_combination:
        print(f" — {action}\n Profit value = {action.profit_value}€")
    print(f"Total cost: \n\t\t{BLD}{best_cost}{NO_STL}€\n"
          f"Potential profit: \n\t\t{BLD}{best_profit}{NO_STL}€ ({total_benef}%)")
