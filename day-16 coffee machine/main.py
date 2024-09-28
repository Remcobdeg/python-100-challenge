from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_menu = Menu()
options = coffee_menu.get_items()
coffee_machine = CoffeeMaker()
money_handler = MoneyMachine()

provit = 0

is_on = True

while is_on:
    print(f'What would you like? {options}: ')
    choice = input().lower()
    if choice in options:
        print("OK")
        drink = coffee_menu.find_drink(choice)
        try:
            print(drink.name)
            if coffee_machine.is_resource_sufficient(drink):
                print(f"Cost {choice}: ${drink.cost}")
                if money_handler.make_payment(drink.cost):
                    provit += drink.cost
                    coffee_machine.make_coffee(drink)
                else:
                    print("Sorry that's not enough money. Money refunded")
        except AttributeError:
            print(f"{choice} is not an menu item")
    elif choice == "off":
        print('Turing off the machine')
        is_on = False
    elif choice == "report":
        print(coffee_machine.report())
        print(money_handler.report())
    else:
        print('not a valid choice, try again.')

