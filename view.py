import functools
from config import BLD, NO_STL, clarify_algo_name


def goldify(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("\033[1;38;5;226m", end="")
        result = func(*args, **kwargs)
        print("\033[0m", end="")
        return result
    return wrapper

def center_(txt):
    return f"{txt:^80}"

@goldify
def display_title(txt):
    print(center_(txt))

def alert_msg(alert_name, msg):
    print(
        f"\n\033[1;5;91m{f'[ {alert_name} ]':^80}\033[0m\n"
        f"{f'{msg}':^80}\n\n"
        )
    input(f"{'':34}")

def bruteforce_warning(actions):
    alert_name = "WARNING"
    msg = (f"{f'Important amount of operations ({len(actions)})':^80}\n"
        f"{'Continue with the brute force method ? ':^80}")
    alert_msg(alert_name, msg)
    return input(f"\n\n{'Yes/No (y/n)?':^80}\n{'':34}")

def display_algorithm(dp=False):
    algo = clarify_algo_name(dp=dp)
    print(f"\n\n{'~~~~~~~~~~~~~~~~~~~~':^80}")
    display_title(algo)
    print(f"{'~~~~~~~~~~~~~~~~~~~~':^80}\n")

def display_selected_actions(total_num_actions, best_cost, best_combination, best_profit, total_benef, dp=False):
    display_algorithm(dp=dp)
    display_title('BEST POSSIBLE COMBINATION')
    print(f"{f'{len(best_combination)} actions sur {total_num_actions}':^80}\n"
        f"{'To see the list of action names, see in /data/output/':^80}\n"
        )
    display_title('TOTAL COST (€)')
    print(f"{BLD}{best_cost:^80}{NO_STL} \n")
    display_title('POTENTIAL PROFIT')
    print(f"\n{f'{best_profit:.2f} € ({total_benef}%)':^80}\n")
    display_title("DETAILS")
    goldify(print)(f"{'  Action Name':^15}   {'Price':>12}    {'Profit (%)':>10}   {'Benef in €':^30}")
    for action in best_combination:
        print(f"{str(action):^80}")




if __name__ == "__main__":
    # actions = [n for n in range(21)]
    # bruteforce_warning(actions)
    # alert_name = input(f"{'Quelle nom d\'alerte ? ':^80}\n{'':34}")
    # msg = input(f"{'Quel message ? ':^80}\n{'':34}")
    # print("\n" * 50)
    # alert_msg(alert_name, msg)
    goldify(display_title)("J'ai FAIM !")
