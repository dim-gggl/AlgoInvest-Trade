import csv
from models import Action

def load_actions(file_path: str="data/Liste_actions.csv"):
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
            action = Action(name=row["Actions #"], cost=row["Coût par action (en euros)"], profit_percentage=row["Bénéfice (après 2 ans)"])
            actions.append(action)
        return actions

if __name__ == "__main__":
    print(load_actions())
