from config import format_percentage_benef, colorize


class Action:
    """
    Represents a financial action with a name, cost, and profit percentage.

    attr:
        name (str): The name of the action.
        id (str): A formatted identifier generated from the name.
        cost (float): The cost of the action in euros. Must be a positive value.
        profit_value (float): The profit percentage of the action.
        profit (float): The calculated profit in euros after 2 years.
    """
    def __init__(
        self,
        name: str,
        cost_value: str | float | int,
        profit_percentage: str | float | int
        ) -> None:

        self.name = name
        self.id = name.split("-")[-1].strip()
        self.cost = float(cost_value)
        try:
            self.profit_value = format_percentage_benef(
                profit_percentage
                )
        except Exception as e:
            print(f"Error : {e}")

        self.profit = self.compute_profit()

    def loss(self):
        if self.profit_value < 0:
            return self.profit_value * -1
        else:
            return None

    def compute_profit(self):
        if self.profit_value > 0:
            return self.cost * self.profit_value * 0.01
        elif self.profit_value == 0:
            return 0
        else:
            print(f"No profit, loss of {self.loss()}%")

    def __str__(self):
        return (
            f"{f'Action # {self.id}':<15} {self.cost:>8} €   "
            f"{f'{self.profit_value}':>8} % "
            f"{f'(about {self.profit:.2f} € profit)':^32}"
            )

    def __repr__(self):
        return (f"Action #{self.id}, Cost={self.cost} €, "
            f"Benefit={self.profit_value}%, Profit={self.profit:.2f} €)")


class CorruptedAction(Action):
    def __init__(
            self,
            name,
            cost_value: str,
            profit_percentage: str
            ) -> None:

        self.name = name
        self.id = name.split("-")[-1].strip()
        self.cost = float(cost_value)
        self.profit_value = float(
            profit_percentage.replace("%", "").strip()
            )
        self.profit = super().compute_profit()

    def __str__(self):
        profit = round(self.profit, 2)
        return (
            f"{f'{self.name}':^17} {colorize(self.cost):^10} €    "
            f"{colorize(self.profit_value):^12}{'%':^5}   "
            f"{f'({colorize(profit)} €)':^22}"
        )

    def __repr__(self):
        return (f"Action #{self.id}, Cost={self.cost} €, "
                f"Benefit={self.profit_value}%, "
                f"Profit={self.profit:.2f} €)")





class ActionPriceError(Exception):
    pass


class PercentageValueError(Exception):
    pass
