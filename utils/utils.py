import csv
from models.models import Action

def load_actions(file_path: str="./data/Liste_actions.csv"):
    """
    Load a list of actions from a CSV file.
    Args:
        file_path (str): The path to the CSV file containing the actions. 
                            Defaults to "./Liste_actions.csv".
    Returns:
        list: A list of Action objects created from the data in the CSV file.
    """
    actions = []
    with open(file_path, "r") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                action = Action(name=row["Actions"], cost=row["Cost"], profit_percentage=row["Benefits"])
                actions.append(action)
            except Exception as e:
                print(f"Ignored action {row}: {e}")
        return actions
