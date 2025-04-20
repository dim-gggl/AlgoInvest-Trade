import functools
from config import BLD, NO_STL, clarify_algo_name


# —————————————— Color tools for the view ————————————————

def goldify(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("\033[1;38;5;226m", end="")
        result = func(*args, **kwargs)
        print("\033[0m", end="")
        return result
    return wrapper

def ansify(func, ansi_color):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"{ansi_color}", end="")
        result = func(*args, **kwargs)
        print("\033[0m", end="")
        return result
    return wrapper

def toxify(txt):
    return f"\033[1;38;5;135m{txt}\033[0m]"

def col_print(color, msg, center=True, small_center=False):
    if center:
        return ansify(print, color)(center_(msg))
    elif small_center:
        return ansify(print, color)(center__(msg))
    else:
        return ansify(print, color)(msg)

# ————————————————— Layout parameters ———————————————————

def center_(txt):
    return f"{txt:^80}"

def center__(txt):
    return f"{txt:^50}"

@goldify
def display_title(txt):
    print(center_(txt))

# —————————————— Messages & Warnings ————————————————

def alert_msg(alert_name, msg):
    print(
        f"\n\033[1;5;91m{f'[ {alert_name} ]':^80}\033[0m\n"
        f"{f'{msg}':^80}\n\n"
        )
    input(f"{'':34}")

def bruteforce_warning(actions):
    alert_name = "WARNING"
    msg = (
        f"{f'Important amount of operations ({len(actions)})':^80}\n"
        f"{'Continue with the brute force method ? ':^80}"
        )
    alert_msg(alert_name, msg)
    return input(f"\n\n{'Yes/No (y/n)?':^80}\n{'':34}")

def bye_msg():
    print("\n" * 50)
    goldify(print)(center_("Bye Bye"))
    print("\n" * 3)
    input(f"{'':34}")

def display_algorithm(dp=False):
    algo = clarify_algo_name(dp=dp)
    print(f"\n\n{'~~~~~~~~~~~~~~~~~~~~':^80}")
    display_title(algo)
    print(f"{'~~~~~~~~~~~~~~~~~~~~':^80}\n")

# ————————————— For collecting User's intentions —————————————————

def get_algorithm_choice():
    print("\n" * 50)
    print(center_("Quel algorithme souahitez-vous appliquer ?"))
    print(center_("1 - Force Brute"))
    print(center_("2 - Programmation Dynamique"))
    print("\n" * 3)
    return input(f"{'Votre choix':^80}\n{'':^39}")

def get_data_paths(comparing=False):
    print("\n" * 50)
    print(center_("Quel fichier voulez-vous explorer ?"))
    if not comparing:
        print(center_("1 - Rester sur Listes_actions.csv"))
        print(center_("2 - Traiter la base de données N°1 "))
        print(center_("3 - Traiter la base de données N°2 "))
    else:
        print(center_("1 - Traiter la base de données N°1 "))
        print(center_("2 - Traiter la base de données N°2 "))
    print("\n" * 3)
    return input(f"{'Votre choix':^80}\n{'':39}")

def ask_for_comparison_display():
    blue = "\033[1;38;5;69m"
    print("\n" * 50)
    col_print(blue, "Afficher la comparaison avec le choix de Sienna ?\n\n")
    print(center_("Yes/No (y/n)\n\n\n"))
    return input(f"{'Your choice : ':^80}\n{'':39}")

def ask_to_see_invoice():
    print("\n")
    print(center__("Voulez-vous voir le détail ?"))
    print(center__("Yes/No"))
    return input(f"{'Votre choix':^50}\n{'':24}")


# —————————————————— For displaying data ———————————————————————————

def display_selected_actions(
        total_num_actions,
        best_cost,
        best_combination,
        best_profit,
        total_benef,
        dp=False
        ):
    print("\n" * 50)
    display_algorithm(dp=dp)
    display_title('BEST POSSIBLE COMBINATION')
    print(
        f"{f'{len(best_combination)} actions over {total_num_actions}':^80}\n"
        f"{'To see the list of action names, see in /data/output/':^80}\n"
        )
    display_title('TOTAL COST (€)')
    print(
        f"{BLD}{best_cost:^80}{NO_STL} \n"
        )
    display_title('POTENTIAL PROFIT')
    print(
        f"\n{f'{best_profit:.2f} € ({total_benef}%)':^80}\n"
        )
    display_title("DETAILS")
    goldify(print)(
        f"{'  Action Name':^15}   {'Price':>12}  "
        f"  {'Profit (%)':>10}   {'Benef in €':^30}"
        )
    for action in best_combination:
        print(f"{str(action):^80}")
    input()

def display_corrupted_actions(
        file_name,
        corrupted_actions,
        total_actions,
        negative_costs,
        null_costs,
        details=False
        ):
    green = "\033[1;38;5;105m"
    print("\n" * 50)
    col_print(
        green,
        "CORRUPTED DATA",
        center=False,
        small_center=True
        )
    print("\n")
    ansify(print, green)(center__(file_name.split(".")[0]))
    print(center__(f"{len(corrupted_actions)}/{total_actions} actions\n"))
    ansify(print, green)(
        center__(
            "NEGATIVE COSTS"
        )
    )
    print(center__(f"{len(negative_costs)}/{total_actions}\n"))
    ansify(print, green)(
        center__(
            "COST = ZERO"
        )
    )
    print(center__(f"{len(null_costs)}/{total_actions}\n"))
    if details:
        ansify(print, green)(
            center__("DETAILS")
            )
        print(center__("~~~~~~~~~~~~~~~~~~~~"))
        for action in corrupted_actions:
            print(center__(str(action)))

def display_details(corrupted_actions):
    green = "\033[1;38;5;105m"
    ansify(print, green)(
        center__("DETAILS")
        )
    print(center__("~~~~~~~~~~~~~~~~~~~~"))
    for action in corrupted_actions:
        print(center__(str(action)))
    input()


def display_comparison(
        file_name,
        algo,
        sienna_total_cost,
        algo_total_cost,
        actions_1,
        actions_2,
        same_actions=None
        ):

    orange = "\033[1;38;5;202m"

    print("\n" * 50)
    col_print(orange, "COMPARISON RESULTS")
    print("\n")
    col_print(orange, algo)
    print(center_(file_name))
    print(
        f"{'SIENNA\'S CHOICE':^40}{'PROGRAM\'S CHOICE':^40}\n"
        )
    print(
        f"{'TOTAL COST':^40}{'TOTAL COST':^40}"
        )
    col_print(
        orange,
        f"{sienna_total_cost:^40}{algo_total_cost:^40}",
        center=False
        )
    if same_actions:
        print(
            center_(
                f"{len(same_actions)} actions in common"
                )
            )
        col_print(
            orange,
            "~~~~~~~ SAME ACTIONS ~~~~~~"
            )
        for action in same_actions:
            print(
                f"{action.name:^40}{action.name:^40}"
                )
    col_print(
        orange,
        "~~~~~~ DIFFERENCES ~~~~~~"
        )
    max_len = max(
                len(actions_1),
                len(actions_2)
                )
    for i in range(max_len):
        name_left = actions_1[i].name if i < len(actions_1) else ""
        name_right = actions_2[i].name if i < len(actions_2) else ""
        print(f"{name_left:^40}{name_right:^40}")
    input()
