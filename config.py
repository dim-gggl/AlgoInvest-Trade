# from models import PercentageValueError, ActionPriceError


BLD = "\033[1m"
NO_STL = "\033[0m"


def format_action_id(string_id) -> int:
    """
    Convert a string action ID into a float 
    after removing the "Action-" prefix.
    Args:
        string_id (str): The string representation 
                         of the action ID.
    Returns:
        int: The converted action ID as a float.
    Raises:
        ActionPriceError: If the string cannot be 
                          converted to a float.
    """
    string_id = string_id.lstrip("Action-").strip()
    try:
        action_id = int(string_id)
        return action_id
    except ValueError:
        raise 

def format_percentage_benef(string_value: str) -> float:
    """
    Converts a percentage string to a float.
    Args:
        string_value (str): The percentage 
                            string (e.g., "50%").
    Returns:
        float: The numeric value of the percentage.
    Raises:
        PercentageValueError: If the string cannot 
                              be converted to a float.
    """
    clear_string = string_value.replace("%", "").strip()
    try:
        clear_benef = float(clear_string)
        return clear_benef
    except ValueError:
        raise 


