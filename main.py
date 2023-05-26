from data import MENU, resources
import bcolors

print(MENU)
print(resources)
QUARTERS = 0.25
DIMES = 0.1
NICKLES = 0.05
PENNIES = 0.01
money = 0
running = True


def print_resources():
    print(bcolors.bcolors.OKBLUE + f"Water: {resources['water']}ml \nMilk: {resources['milk']}ml \nCoffee: "
                                   f"{resources['coffee']}g \nMoney: ${money}" + bcolors.bcolors.ENDC)


def insert_coins():
    print("Please insert coins.")
    inserted_quarters = int(input("How many quarters?: "))
    inserted_dimes = int(input("How many dimes?: "))
    inserted_nickles = int(input("How many nickles?: "))
    inserted_pennies = int(input("How many pennies?: "))
    sum_money = QUARTERS * inserted_quarters + DIMES * inserted_dimes + NICKLES * inserted_nickles \
        + PENNIES * inserted_pennies
    print(sum_money)
    return round(sum_money, 2)


def check_and_calculate_money(inserted_money, coffee_price):
    print(inserted_money, coffee_price)
    if inserted_money > coffee_price:
        print(f"Here is ${inserted_money - coffee_price} in change.")
    elif inserted_money == coffee_price:
        print("There is no change as exact money has been inserted.")
    elif inserted_money < coffee_price:
        print(f"Sorry there is not enough money. You need ${coffee_price - inserted_money} more. Money refunded.")
    else:
        print("Unexpected action!")


while running:
    user_input = input("What would you like? (espresso/latte/cappuccino): \n")
    if user_input == "report":
        print_resources()
    elif user_input == "latte":
        money = insert_coins()
        check_and_calculate_money(money, MENU["latte"]["cost"])
    elif user_input == "off":
        print(bcolors.bcolors.FAIL + "Turning OFF..." + bcolors.bcolors.ENDC)
        running = False
