import csv, json, sys
from models import Action
from config import clarify_algo_name
from view import bruteforce_warning


def get_csv_headers(filepath, delimiter=',', encoding='utf-8'):
    with open(filepath, mode='r', encoding=encoding) as f:
        reader = csv.reader(f, delimiter=delimiter)
        headers = next(reader)
    return headers

def load_actions(
        file_path: str="data/Liste_actions.csv",
        with_dirt=False
        ) -> tuple[list[Action], list[str]] | list[Action]:
    """
    Load actions from a CSV file, separating valid actions and invalid data.
    When used to generate a repport, the arg with_dirt is set on True, so it
    will also return a list of obsolete actions.

    Args:
        file_path (str):
                        Path to the CSV file (default: "data/Liste_actions.csv").
        with_dirt (bool):
                        If set on True, returns the liste of unusable data.
                        Default on False.
    Returns:
        tuple:  (valid actions as Action objects, invalid rows as dicts).
    """

    # Since the headers are different from one CSV to another,
    # we start by collecting the headers of the common file.

    headers = get_csv_headers(file_path)
    list_actions = []
    corrupted_data = []
    with_dirt = with_dirt
    with open(file_path, "r") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:

                # We check the data to confirm it is valid and usable

                price = float(row[headers[1]])
                profit = float(
                    row[headers[2]].rstrip("%")
                    )

                # Obviously the cost of an action cannot be 0,
                # so if it's the case,
                # we assume the data is obsolete.

                if price > 0 and profit >=  0:
                    action = Action(
                        name=row[headers[0]],
                        cost_value=row[headers[1]],
                        profit_percentage=row[headers[2]]
                        )
                    list_actions.append(action)

                # We apply the same logic for a price that is negative

                elif float(row[headers[1]]) <= 0:
                    corrupted_data.append(row)

            # And eventually, we consider that if, by converting a price into
            # a float, we raise an exception, it's also a sign of corrupted
            # data.

            except ValueError:
                corrupted_data.append(row)
        if with_dirt:
            return list_actions, corrupted_data
        else:
            return list_actions

def save_ouput(
        src_name:str,
        data_list:list,
        dp:bool=False
        ):

    # This function cleans the file name frop its path
    # in order to name the output file with a similar
    # name to stay easily identifiable.

    src_name = src_name.split("/")[-1].split(".")[0]
    algo = clarify_algo_name(dp=dp)
    title =  f"{algo}_{src_name}"
    file_name = title.lower().replace(" ", "_")
    file_path = f"data/output/{file_name}.json"

    # It only stores the actions ids in a json file
    # so we need another function to invoke the actions
    # objects back when loading.

    data = [action.id for action in data_list]
    with open(file_path, "w") as f:
        json.dump(data, f, ensure_ascii=True, indent=4)

def load_actions_from_name(
        action_names: list[str],
        src_file:str
        ) -> list[Action]:
    """
    From a list of action names and the dataset path where
    these actions are from, recreates the action objects and
    return them in a list
    Args:
        action_names (list):
                        Should be a list of string containing
                        action names.
        src_file (str):
                    Should be a str containins the path to
                    the original csv file where the actions can
                    be found.
    Returns::
            (list): containing the action objects with the
            matching name.
    """
    extracted_actions = []
    with open(src_file, "r") as file:
        reader = csv.DictReader(file)
        headers = get_csv_headers(filepath=src_file)
        for row in reader:
            if row[headers[0]] in action_names:
                extracted_actions.append(
                    Action(
                        name=row["name"],
                        cost_value=row["price"],
                        profit_percentage=row["profit"]
                        )
                    )
    return extracted_actions

# Here we are looking for some arguments that might have been passed
# while lauching the script. Such as "-dp" or "-f"

def are_args() -> bool:
    return len(sys.argv[1:]) > 0

def parse_cli_args():

    # By default we assume the app has been opened directly
    # so we specify a path and folder where to gather
    # these informations.

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

    # Here, we handle the user's choices about the file to
    # process and the algorith to apply.

    if is_optimized:
        return True
    if len(actions) <= 20:
        return False

    # Also, we display a warning if the brute force
    # method is chosen with an important dataset.

    choice = bruteforce_warning(actions).strip().lower()
    print(choice)
    if choice == "y":
        return False
    input(
        f"\n\n{'Let\'s try the optimized algorithm !':^70}\n{'':34}"
    )
    return True

def calculate_total_benefit(
        best_profit,
        best_cost,
        best_combination
        ):
    try:
        return round(
            best_profit * 100 / best_cost, 2
            )
    except ZeroDivisionError:
        print(
            f"{best_profit=}, "
            f"{[str(a) for a in best_combination]} {best_cost=}"
        )
        return 0
