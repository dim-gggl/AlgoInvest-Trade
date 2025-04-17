import sys
from bruteforce import brute_force
from optimized import optimized
from config import BLD, NO_STL
from view import bruteforce_warning, display_selected_actions
from utils import (
    load_actions,
    save_ouput,
    parse_cli_args,
    choose_algorithm,
    calculate_total_benefit
)

"""
This function executes both algorithms of the program
on the available data sources.

Note: You can pass options directly via the terminal:

    Usage: python3 main.py <options>

Options:
  -dp        Run the script with the dynamic programming algorithm.
              Defaults to 'Brute Force'.
  -f <path>  Specify the CSV file to analyze.

Args:
    file_path: Path to the CSV file. Defaults to "data/Liste_actions.csv".
               Can also accept "data/Dataset_1.csv" or "data/Dataset_2.csv".

Returns:
    tuple:
      - float: The total cost of the selected actions.
      - list:  A list of the corresponding Action instances.
      - float: The total profit.
"""
def main(file_path:str, is_optimized=False) -> None:
    actions = load_actions(file_path)
    budget = 500
    is_optimized = choose_algorithm(
        actions, is_optimized
        )
    if is_optimized:
        run_algo = optimized
    else:
        run_algo = brute_force

    best_cost, best_combination, best_profit = run_algo(
        actions=actions, budget=budget
    )

    total_benef = calculate_total_benefit(
        best_profit, best_cost, best_combination
        )

    display_selected_actions(
        len(actions),
        best_cost,
        best_combination,
        best_profit,
        total_benef,
        dp=is_optimized
    )

    save_ouput(
        src_name=file_path,
        data_list=best_combination,
        dp=is_optimized
        )

if __name__ == "__main__":
    file_path, dp = parse_cli_args()
    main(file_path=file_path, is_optimized=dp)
