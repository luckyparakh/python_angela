from CoffeeMachine.art import logo
from CoffeeMachine.data import MENU, resources

print(logo)


def resources_check(coffee_type):
    if resources['water'] < MENU[coffee_type]['ingredients']['water']:
        return 'water'
    if resources['coffee'] < MENU[coffee_type]['ingredients']['coffee']:
        return 'coffee'
    if coffee_type != 'espresso' and resources['milk'] < MENU[coffee_type]['ingredients']['milk']:
        return 'milk'
    return ""


def print_resources():
    print(f"""
    'Water': {resources['water']}
    'Milk': {resources['milk']}
    'Coffee': {resources['coffee']}
    'Money': {resources['money']}
    """)


def serve_coffee(coffee_type):
    resource_depleted = resources_check(coffee_type)
    if resource_depleted:
        print(f"Sorry there is not enough {resource_depleted}")
        return
    else:
        print("Please insert coins.")
        quarters = int(input("How many quarters?"))
        dimes = int(input("How many dimes?"))
        nickles = int(input("How many nickles?"))
        pennies = int(input("How many pennies?"))
        total_money = 0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies
        if total_money >= MENU[coffee_type]['cost']:
            if total_money > MENU[coffee_type]['cost']:
                change = total_money - MENU[coffee_type]['cost']
                print(f"Here is ${change:.2f} dollars in change ")
            resources['money'] += MENU[coffee_type]['cost']
            resources['water'] -= MENU[coffee_type]['ingredients']['water']
            resources['coffee'] -= MENU[coffee_type]['ingredients']['coffee']
            if coffee_type != 'espresso':
                resources['milk'] -= MENU[coffee_type]['ingredients']['milk']
        else:
            print("Sorry that's not enough money. Money refunded.")
            return


def coffee_machine():
    continue_flag = True
    resources['money'] = 0
    while continue_flag:
        coffee_type = input("What would you like? (espresso/latte/cappuccino):").lower()
        if coffee_type == 'off' :
            print ("Switching Off the Machine.")
            continue_flag = False
        elif coffee_type == 'report':
            print_resources()
        elif coffee_type in ('espresso', 'latte', 'cappuccino'):
            serve_coffee(coffee_type)
        else:
            print("Wrong input. Try Again!!")


coffee_machine()

