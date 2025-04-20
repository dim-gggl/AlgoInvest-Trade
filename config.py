def colorize(val: float) -> str:
    if val < 0:
        col = "\033[1;38;5;196m"
    elif val == 0:
        col = "\033[1;38;5;214m"
    else:
        col = "\033[1;38;5;14m"
    return f"{col}{val:.2f}\033[0m"

BLD = "\033[1m"
NO_STL = "\033[0m"

def format_percentage_benef(string_value:str) -> float:
    string_value = str(string_value).strip()
    if "%" in string_value:
        string_value = string_value.replace("%", "")
    try:
        clear_benef = float(string_value)
        return clear_benef
    except ValueError:
        raise

def clarify_algo_name(dp=False) -> str:
    if not dp:
        return "BRUTE FORCE"
    else:
        return "DYNAMIC PROGRAMMING"
