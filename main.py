from utils import load_actions
from bruteforce import brute_force
from optimized import optimized
from config import BLD, NO_STL


def main(actions=load_actions, budget=500, file_path='data/Liste_actions.csv', is_optimized=False):
    actions = actions(file_path)
    budget = budget
    run_algo = None
    if not is_optimized and len(actions) > 20:
        print(
            f"\n{'-[ \033[1;5;91mWARNING\033[0m ]-':^70}\n{f'Important amount of operations ({len(actions)})':^70}\n"
            f"{'Continue with the brute force method ? ':^70}"
            )
        choice = input(f"\n\n{'Yes/No (y/n)?':^70}\n{'':35}").strip().lower()
        if choice == "y":
            run_algo = brute_force
        else:
            input("\n\n" + f"{'We should try with the optimized algorithm, safer !':70}\n{"":35}")
            run_algo = optimized
    else:
        run_algo = optimized

    best_cost, best_combination, best_profit = run_algo(actions=actions, budget=budget)
    if is_optimized:
        best_combination.reverse()
    try:
        total_benef = round(best_profit * 100 / best_cost, 2)
    except ZeroDivisionError:
        print(f"{best_profit=}, {[str(a) for a in best_combination] if best_combination else None} {best_cost=}")
        total_benef = 0
    print(f"\n\n{'BEST POSSIBLE COMBINATION':^70} \n{', '.join([str(action.id) for action in best_combination]):^70}")
    print(f"\n{'TOTAL COST (€)':^70}\n{BLD}{best_cost:^70}{NO_STL} \n"
          f"\n{'POTENTIAL PROFIT ':^70}\n{f'{best_profit:.2f} € ({total_benef}%)':^70}\n")
    print(f"\n{'DETAILS':^70}\n")
    for action in best_combination:
        print(f"{str(action):^70}")

if __name__ == "__main__":
    main(is_optimized=True)
