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
    "milk": 200,
    "coffee": 100,
    "money": 0
}


def check_resources(choice_):
    ingredients = (MENU[choice_]['ingredients'])
    for ingredient in ingredients:
        if resources[ingredient] < ingredients[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
    return True


def process_coins():
    print("Please insert coins.")
    quarters = int(input("Quarters: "))
    dimes = int(input("Dimes: "))
    nickles = int(input("Nickles: "))
    pennies = int(input("Pennies: "))
    total = round(quarters * .25 + dimes * .10 + nickles * .05 + pennies * .01, 2)
    print(f"Funds: {total}")
    return total


def process_resources(choice_, funds_):
    ingredients = (MENU[choice_]['ingredients'])

    # adjust machine resources
    resources["money"] += MENU[choice]['cost']
    for ingredient in ingredients:
        resources[ingredient] -= ingredients[ingredient]

    # refund remaining money
    refund = round(funds_ - MENU[choice]['cost'], 2)
    if refund >= 0.01:
        print(f"Here is ${refund} dollars in change.")

    # make coffee
    print(f'serving {choice}')

    return resources


is_on = True

while is_on:
    choice = input('What would you like? (espresso/latte/cappuccino): ').lower()
    if choice in ["espresso","latte","cappuccino"]:
        sufficient_resources = check_resources(choice)
        if sufficient_resources:
            cost = MENU[choice]['cost']
            print(f"Cost: ${cost}")
            funds = process_coins()
            if funds >= MENU[choice]['cost']:
                resources = process_resources(choice,funds)
            else:
                print("Sorry that's not enough money. Money refunded")
    elif choice == "off":
        print('Turing off the machine')
        is_on = False
    elif choice == "report":
        print(resources)
    else:
        print('not a valid choice, try again.')








