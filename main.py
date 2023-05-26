from data import MENU, resources
import bcolors

QUARTERS = 0.25
DIMES = 0.1
NICKLES = 0.05
PENNIES = 0.01

# Resources
water = resources['water']
milk = resources['milk']
coffee = resources['coffee']
money = 0

running = True

coffee_costs = {}

for coffee_name, details in MENU.items():
    cost = details["cost"]
    coffee_costs[coffee_name.upper()] = cost

for coffee_name, cost in coffee_costs.items():
    print(bcolors.bcolors.HEADER + f"{coffee_name}: ${cost}" + bcolors.bcolors.ENDC)


def print_resources():
    print(bcolors.bcolors.OKBLUE + f"Water: {water}ml \nMilk: {milk}ml \nCoffee: {coffee}g \nMoney: ${money}" +
          bcolors.bcolors.ENDC)


def refill():
    global water, milk, coffee
    water = resources['water']
    milk = resources['milk']
    coffee = resources['coffee']


def insert_coins():
    print("Please insert coins.")
    inserted_quarters = int(input("How many quarters?: "))
    inserted_dimes = int(input("How many dimes?: "))
    inserted_nickles = int(input("How many nickles?: "))
    inserted_pennies = int(input("How many pennies?: "))
    sum_money = QUARTERS * inserted_quarters + DIMES * inserted_dimes + NICKLES * inserted_nickles \
        + PENNIES * inserted_pennies
    return round(sum_money, 2)


def check_and_calculate_money(added_money, coffee_price):
    if added_money > coffee_price:
        print(bcolors.bcolors.OKBLUE + f"Here is ${round(added_money - coffee_price, 2)} in change." +
              bcolors.bcolors.ENDC)
    elif added_money == coffee_price:
        print("There is no change as exact money has been inserted.")
    elif added_money < coffee_price:
        print(f"Sorry there is not enough money. You need ${round(coffee_price - added_money, 2)} more. "
              f"Money refunded.")
        return False
    else:
        print("Unexpected action!")
        return False
    return True


def check_resources(requested_coffee):
    not_enough_resources = []
    if water < MENU[requested_coffee]["ingredients"]["water"]:
        not_enough_resources.append("water")
    if milk < MENU[requested_coffee]["ingredients"].get("milk", 0):
        not_enough_resources.append("milk")
    if coffee < MENU[requested_coffee]["ingredients"]["coffee"]:
        not_enough_resources.append("coffee")

    if bool(not_enough_resources):
        print(bcolors.bcolors.RED + "Sorry, not enough " + ", ".join(not_enough_resources) + "." + bcolors.bcolors.ENDC)
        return False
    return True


def update_resources(coffee_type):
    global water
    global milk
    global coffee
    global money
    water -= MENU[coffee_type]["ingredients"]["water"]
    milk -= MENU[coffee_type]["ingredients"].get("milk", 0)
    coffee -= MENU[coffee_type]["ingredients"]["coffee"]
    money += MENU[coffee_type]["cost"]


while running:
    user_input = input("What would you like? (espresso/latte/cappuccino): \n").lower()
    if user_input == "report":
        print_resources()
    elif user_input == "espresso":
        if check_resources(user_input):
            inserted_money = insert_coins()
            if check_and_calculate_money(inserted_money, MENU[user_input]["cost"]):
                update_resources(user_input)
                print(bcolors.bcolors.HEADER + f"Here is your {user_input} ☕" + bcolors.bcolors.ENDC)
    elif user_input == "latte":
        if check_resources(user_input):
            inserted_money = insert_coins()
            if check_and_calculate_money(inserted_money, MENU[user_input]["cost"]):
                update_resources(user_input)
                print(bcolors.bcolors.HEADER + f"Here is your {user_input} ☕" + bcolors.bcolors.ENDC)
    elif user_input == "cappuccino":
        if check_resources(user_input):
            inserted_money = insert_coins()
            if check_and_calculate_money(inserted_money, MENU[user_input]["cost"]):
                update_resources(user_input)
                print(bcolors.bcolors.HEADER + f"Here is your {user_input} ☕" + bcolors.bcolors.ENDC)
    elif user_input == "refill":
        refill()
    elif user_input == "off":
        print(bcolors.bcolors.RED + "Turning OFF..." + bcolors.bcolors.ENDC)
        running = False
