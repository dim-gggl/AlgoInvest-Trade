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
