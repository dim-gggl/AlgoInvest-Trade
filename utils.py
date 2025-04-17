import csv, json
from models import Action
from config import clarify_algo_name
from view import bruteforce_warning


def get_csv_headers(filepath, delimiter=',', encoding='utf-8'):
    with open(filepath, mode='r', encoding=encoding) as f:
        reader = csv.reader(f, delimiter=delimiter)
        headers = next(reader)
    return headers

def load_actions(file_path: str="data/Dataset_1.csv", with_dirt=False) -> tuple[list[Action], list[str]]:
    """
    Load actions from a CSV file, separating valid actions and invalid rows.
    Args:
        file_path (str): Path to the CSV file (default: "data/Dataset_1.csv").
    Returns:
        tuple: (valid actions as Action objects, invalid rows as dicts).
    """
    headers = get_csv_headers(file_path)
    list_actions = []
    corrupted_data = []
    with_dirt = with_dirt
    with open(file_path, "r") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                price = float(row[headers[1]])
                profit = float(row[headers[2]].rstrip("%"))
                if price > 0 and profit >=  0:
                    action = Action(
                        name=row[headers[0]],
                        cost_value=row[headers[1]],
                        profit_percentage=row[headers[2]]
                        )
                    list_actions.append(action)
                elif float(row[headers[1]]) < 0 or float(row[headers[2]].rstrip("%")) < 0:
                    corrupted_data.append(row)
            except ValueError:
                print(f"{row[headers[0]]} - {row[headers[1]]} - {row[headers[2]]}")
                corrupted_data.append(row)
        if with_dirt:
            return list_actions, corrupted_data
        else:
            return list_actions

def save_ouput(src_name, data_list, dp=False):
    src_name = src_name.split("/")[-1].split(".")[0]
    algo = clarify_algo_name(dp=dp)
    title =  f"{algo}_{src_name}"
    file_name = title.lower().replace(" ", "_")
    file_path = f"data/output/{file_name}.json"
    data = [action.id for action in data_list]
    with open(file_path, "w") as f:
        json.dump(data, f, ensure_ascii=True, indent=4)

def parse_cli_args():
    import sys
    file_path = "data/Liste_actions.csv"
    dp = False
    args = sys.argv[1:] if len(sys.argv) > 1 else []
    for i, arg in enumerate(args[:-1]):
        if arg == "-f":
            file_path = args[i+1]
    if "-dp" in args:
        dp = True
    return file_path, dp

def choose_algorithm(actions, is_optimized):
    if is_optimized:
        return True
    if len(actions) <= 20:
        return False
    choice = bruteforce_warning(actions).strip().lower()
    print(choice)
    if choice == "y":
        return False
    input(
        f"\n\n{'Let\'s try the optimized algorithm !':^70}\n{'':34}"
    )
    return True

def calculate_total_benefit(best_profit, best_cost, best_combination):
    try:
        return round(best_profit * 100 / best_cost, 2)
    except ZeroDivisionError:
        print(
            f"{best_profit=}, "
            f"{[str(a) for a in best_combination]} {best_cost=}"
        )
        return 0

# if __name__ == "__main__":
#     actions, corrupted_data = load_actions()
#     print(actions)
#     print(corrupted_data)
