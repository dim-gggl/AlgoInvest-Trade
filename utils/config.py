def format_action_id(string_id) -> int:
    string_id = string_id.lstrip("Action-").strip()
    action_id = int(string_id)
    return action_id

def format_percentage_benef(string_value: str) -> float:
    clear_string = string_value.replace("%", "").strip()
    clear_benef = float(clear_string)
    return clear_benef

BLD = "\033[1m"
NO_STL = "\033[0m"
