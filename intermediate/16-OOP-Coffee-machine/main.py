from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

on = True

while on:
    options = menu.get_items()
    order = input(f"What would you like? ({options}) ")
    if order == 'report':
        coffee_maker.report()
        money_machine.report()
    elif order == 'off':
        on = False
    else:
        drink_order = menu.find_drink(order)
        print(f"The cost is {drink_order.cost}")
        if coffee_maker.is_resource_sufficient(drink_order):
            if money_machine.make_payment(drink_order.cost):
                coffee_maker.make_coffee(drink_order)