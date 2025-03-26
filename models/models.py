from utils.config import format_action_id, format_percentage_benef


class ActionPriceValueError(Exception):
    pass

class Action:
    """
    Represents a financial action with a name, cost, and profit percentage.

    Attributes:
        name (str): The name of the action.
        id (str): A formatted identifier generated from the name.
        cost (float): The cost of the action in euros. Must be a positive value.
        profit_percentage (float): The profit percentage of the action.
        profit_value (float): The calculated profit in euros after 2 years.
    """
    def __init__(self, name: str, cost: str, profit_percentage: str):
        self.name = name
        try:
            # Format or generate the ID from the name
            self.id = format_action_id(name)
        except (TypeError, ValueError) as e:
            raise ValueError("Invalid name or ID for the action : " + str(e))

        # Conversion and validation of the cost
        try:
            cost_value = float(cost)
            if cost_value <= 0:
                raise ActionPriceValueError("The action cost must be positive")
            self.cost = cost_value
        except ValueError:
            raise ActionPriceValueError("The cost must be convertible to a float")

        # Conversion of the profit percentage
        try:
            self.profit_percentage = format_percentage_benef(profit_percentage)
        except ValueError:
            raise ValueError("The profit must be convertible to a float")

        # Calculation of profit in euros after 2 years
        self.profit_value = self.cost * self.profit_percentage / 100

    def __str__(self):
        return (f"Action #{self.id}: Cost = {self.cost} €, "
                f"Benefit = {self.profit_percentage}% "
                f"(about {self.profit_value:.2f} € profit)")

    def __repr__(self):
        return (f"Action #({self.id}, Cost={self.cost} €, "
            f"Benefit={self.profit_percentage}%, Profit={self.profit_value:.2f} €)")
