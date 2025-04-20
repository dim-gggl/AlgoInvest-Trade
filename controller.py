import sys

from bruteforce import brute_force
from optimized import optimized
from view import (
    display_selected_actions,
    get_algorithm_choice,
    get_data_paths,
    alert_msg,
    display_comparison,
    ask_for_comparison_display,
    bye_msg
)
from utils import (
    load_actions,
    load_actions_from_name,
    save_ouput,
    parse_cli_args,
    choose_algorithm,
    calculate_total_benefit,
    are_args,
)
from comparison import (
    extract_actions_from_txt,
    compare_actions
    )


class Controller:

    @classmethod
    def get_info(cls):
        """
        Determines the dataset to analyze and the algorithm to
        use. Goes through multiple processes, starting by checking
        for arguments passed with the script in the beginning

        Reurns:
            - file_path (str):
                            The actual file_path to the dataset
                            that needs to get analyzed.
            - dp (bool):
                        If set on True, tells the main command
                        to launch the Dynamic Programming
                        algorithm. Default on False, which choose
                        the brute force method.
        """
        file_path = ""
        dp = False
        option_1 = {
            "1": False,
            "2": True
        }
        option_2 = {
            "1": "data/Liste_actions.csv",
            "2": "data/dataset1.csv",
            "3": "data/dataset2.csv"
        }
        if are_args():
            file_path, dp = parse_cli_args()
        else:
            try:
                choice = get_algorithm_choice().strip()
                if choice not in option_1.keys():
                    alert_msg(
                        f"WRONG INPUT",
                        f"We select the default file : ({e})"
                        )
                    dp = False
                else:
                    dp = option_1.get(choice)
            except (KeyError, ValueError, TypeError) as e:
                print(e)
                dp = False

            if not file_path:
                try:
                    data_choice = get_data_paths().strip()
                    if choice not in option_2.keys():
                        file_path = "data/Liste_actions.csv"
                    else:
                        file_path = option_2.get(data_choice)
                except ValueError or KeyError as e:
                    alert_msg("WRONG INPUT", e)
                    file_path = "data/Liste_actions.csv"
        return file_path, dp


    @classmethod
    def run_app(cls, file_path:str, is_optimized=False) -> None:
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
        if file_path != "data/Liste_actions.csv":
            Controller.run_comparison_script(file_path)

    @classmethod
    def run_comparison_script(cls, src_file):
        decision = ask_for_comparison_display().strip().lower()
        if decision == "n":
            bye_msg()
            sys.exit()
        elif decision == "y":
            files = {
            "data/dataset1.csv": "data/solution1.txt",
            "data/dataset2.csv": "data/solution2.txt"
            }
            src_file = src_file
            file_path = files.get(src_file)
            file_name = file_path.split("/")[-1]
            action_names = extract_actions_from_txt(
                file_path=file_path,
                destination_file=f"data/output/{file_name}_comparison.csv"
                )
            siennas_actions = load_actions_from_name(
                action_names=action_names,
                src_file=src_file
                )
            siennas_total_cost = sum(
                [action.cost for action in siennas_actions]
                )
            actions = load_actions(file_path=src_file)
            algo_total_cost, algo_actions, _ = optimized(
                                                actions=actions,
                                                budget=500
                                                )
            same_actions = 0
            siennas_spec = None
            algos_spec = None
            same_actions, siennas_spec, algos_spec = compare_actions(
                                                        siennas_actions,
                                                        algo_actions
                                                        )


            display_comparison(
                file_name=file_name,
                algo="DYNAMIC PROGRAMMING",
                sienna_total_cost=siennas_total_cost,
                algo_total_cost=algo_total_cost,
                actions_1=siennas_spec,
                actions_2=algos_spec,
                same_actions=same_actions
                )
        else:
            alert_msg(
                "WRONG INPUT",
                "We did not get your answer. Please try again soon"
                )
