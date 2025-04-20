import csv
from utils import load_actions_from_name, load_actions
from optimized import optimized
from view import display_comparison, get_data_paths

def extract_actions_from_txt(
        file_path="data/solution2.txt",
        destination_file="data/output/siennas_choice.csv"
        ):
    """
    Extracts action informations from a txt file and save it
    to a csv file. Also returns a list of the action names
    Args:
        file_path (str):
                        The actual file path where to extract
                        the information from.
        destination_file (str):
                            The path of the file where to save
                            the extracted information.
    Returns:
        (list): Containing the extracted action names.
    """
    with open(file_path, "r") as f:
        lines = f.readlines()
    data = []
    action_names = []
    for line in lines:
        if line.startswith(("Share-", "Action-")):
            try:
                name, cost = line.strip().split()
                data.append((name, cost))
            except ValueError:
                name = line.strip().split()[0]
            action_names.append(name)
    isolated_actions = [
        name for name in action_names if name not in data
        ]

    with open(
        destination_file,
        "w",
        newline="",
        encoding="utf-8"
        ) as f:
        writer = csv.writer(f)
        writer.writerow(["name", "cost"])
        writer.writerows(data)
        writer.writerows(isolated_actions)
    return action_names


def compare_actions(actions_1, actions_2):
    """
    Compare two lists of actions and return:
        - same: actions present in both lists
        - only_1: actions only in actions_1
        - only_2: actions only in actions_2
    """
    names_1 = {
        action.name: action for action in actions_1
        }
    names_2 = {
        action.name: action for action in actions_2
        }
    same = [
        names_1[name] for name in names_1 if name in names_2
        ]
    only_1 = [
        action for name, action in names_1.items() if name not in names_2
        ]
    only_2 = [
        action for name, action in names_2.items() if name not in names_1
        ]
    return same, only_1, only_2


if __name__ == "__main__":
    choices = {
        "1" : ["data/dataset1.csv", "data/solution1.txt"],
        "2": ["data/dataset2.csv", "data/solution2.txt"]
    }
    choice = get_data_paths(comparing=True)
    src_file = choices.get(choice)[0]
    file_path = choices.get(choice)[1]
    file_name = choices.get(choice)[0].split("/")[-1]
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
    algo_total_cost, algo_actions, algo_profit = optimized(
        actions=actions, budget=500
        )
    same_actions = 0
    siennas_spec = None
    algos_spec = None
    same_actions, siennas_spec, algos_spec = compare_actions(
        siennas_actions, algo_actions
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
