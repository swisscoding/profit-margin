#!/usr/local/bin/python3
# Made by @swisscoding on Instagram

from colored import stylize, fg

# decoration
print(stylize("\n---- | Calculate profit margin | ----\n", fg("red")))

# class
class ProfitMargin:
    def __init__(self, price1, price2):
        self.price1 = price1
        self.price2 = price2

    # output magic method
    def __repr__(self):
        profit_margin = stylize(self.calculate_profit_margin(self.price1, self.price2), fg("green"))
        return f"\nProfit margin is equal to {profit_margin}%.\n"

    # methods
    def calculate_profit_margin(self, p1, p2):
        return str(round(((p2 - p1) / p2) * 100, 2))

# main execution
if __name__ == "__main__":
    # user interaction
    cost_price = float(input("Enter cost price: "))
    sales_price = float(input("Enter sales price: "))

    print(ProfitMargin(cost_price, sales_price))
