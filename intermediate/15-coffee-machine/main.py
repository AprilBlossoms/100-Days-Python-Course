MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 0,
    "coffee": 100,
    "money": 0
}

on = True
def check_resources(order):
    for ingredient in MENU[order]['ingredients']:
        if resources[ingredient] < MENU[order]['ingredients'][ingredient]:
            print(f"Sorry, there is not enough {ingredient}.")
            return
    return True

def check_payment(cost, paid):
    if paid >= cost:
        return True

while on:
    order = input("What would you like? (espresso/latte/cappuccino) ")
    if order == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${resources['money']}")
    elif order == 'off':
        on = False
    else:
        if check_resources(order):
            print(f"The cost is ${MENU[order]['cost']}.")
            quarters = int(input("How many quarters will you use? ")) * .25
            dimes = int(input("How many dimes? ")) * .1
            nickels = int(input("How many nickels? ")) * .05
            pennies = int(input("How many pennies? ")) * .01
            total_inserted = quarters + dimes + nickels + pennies
            if check_payment(MENU[order]['cost'], total_inserted):
                for ingredient in MENU[order]['ingredients']:
                    resources[ingredient] -= MENU[order]['ingredients'][ingredient]
                resources['money'] += MENU[order]['cost']
                change_due = round(total_inserted - MENU[order]['cost'], 2)
                print(f"Your change is ${change_due}.")
                print(f"Here is your {order}. Enjoy!")
            else:
                print("Not enough money")

        


