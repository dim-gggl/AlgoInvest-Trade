import csv, sys
from models import CorruptedAction
from utils import load_actions
from view import (
    get_data_paths,
    display_corrupted_actions,
    ask_to_see_invoice,
    display_details,
    bye_msg,
    alert_msg
    )




"""
In this module, we focus on collecting and siplaying different stats and data.
We seperated for as much as possible avery little task in order to keep it
readable.
"""

def get_file_name(file_path: str) -> str:
    return file_path.split('/')[-1] if '/' in file_path else file_path

def get_cleared_file_path(file_name: str) -> str:
    return f"data/scanned/CLEARED_{file_name}"

def get_report_file_path(file_name: str) -> str:
    return f"data/scanned/REPPORT_{file_name}"

def process_dirty_data(file_path: str) -> list:
    _, dirty_data = load_actions(file_path=file_path, with_dirt=True)
    # Return a list of dictionary rows
    return [row for row in dirty_data]

def get_newlines(
        file_path: str,
        processed_dirty_data: list
        ) -> list:
    newlines = []
    with open(file_path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if not row in processed_dirty_data:
                newlines.append(row)
    return newlines

def write_cleared_file(
        cleared_file_path: str,
        newlines: list
        ):
    with open(cleared_file_path, 'w') as file:
        writer = csv.DictWriter(
            file, ['name', 'price', 'profit']
            )
        writer.writerows(newlines)

def write_report_file(report_file_path: str, processed_dirty_data: list):
    with open(report_file_path, 'w', newline="\n") as r:
        writer = csv.DictWriter(r, ["name", "price", "profit"])
        writer.writerows(processed_dirty_data)

# Here is the main function of the module, calling
# the other ones from this point.

def report_corrupted_data(file_path="data/dataset1.csv"):
    file_name = get_file_name(file_path)
    cleared_file_path = get_cleared_file_path(file_name)
    report_file_path = get_report_file_path(file_name)

    processed_dirty_data = process_dirty_data(file_path)
    newlines = get_newlines(file_path, processed_dirty_data)

    write_cleared_file(cleared_file_path, newlines)
    write_report_file(report_file_path, processed_dirty_data)
    return processed_dirty_data, newlines


if __name__ == "__main__":
    files = {
        "1": "data/dataset1.csv",
        "2": "data/dataset2.csv"
    }
    choice = get_data_paths(comparing=True)
    file_path = files.get(choice)
    file_name = file_path.split("/")[-1]
    corrupted_actions, cleared_actions = report_corrupted_data(file_path)
    processed_actions = corrupted_actions + cleared_actions
    total_actions = len(processed_actions)
    dirty_actions =[]
    for action in corrupted_actions:
            dirty_action = CorruptedAction(
                action["name"],
                action["price"],
                action["profit"]
                )
            dirty_actions.append(dirty_action)
    dirty_actions.sort(key=lambda a: a.cost)
    negative_costs = []
    null_costs = []
    for action in dirty_actions:
        if action.cost < 0:
            negative_costs.append(action)
        elif action.cost == 0:
            null_costs.append(action)

    display_corrupted_actions(
       file_name=file_name,
       corrupted_actions=dirty_actions,
       total_actions=total_actions,
       negative_costs=negative_costs,
       null_costs=null_costs
       )
    choice = ask_to_see_invoice().strip().lower()
    if choice == "y":
        display_details(dirty_actions)
    elif choice == "n":
        bye_msg()
        sys.exit()
    else:
        alert_msg(
            "WRONG INPUT",
            "Erreur de saisie, merci de réessayer bientôt"
            )
        sys.exit()
