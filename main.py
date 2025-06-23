
from data import MENU, resources

money = 0

def report():
    for i in resources:
        if i == "coffee":
            print(f"Coffee: {resources[i]}g")
        else:
            print(f"{i.capitalize()}: {resources[i]}ml")
    print(f"Money: ${money}")

def is_sufficient_ingredients(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources.get(item, 0):
            print(f"Sorry, not enough {item}.")
            return False
    return True

def process_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))
    total = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
    return total

def is_transaction_successful(received_money, cost):
    global money
    if received_money >= cost:
        change = round(received_money - cost, 2)
        if change > 0:
            print(f"Here is your change: ${change}")
        money += cost
        return True
    else:
        print("Sorry, not enough money. Refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕. Enjoy!")

is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        report()
    elif choice in MENU:
        drink = MENU[choice]
        if is_sufficient_ingredients(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
    else:
        print("Invalid input. Try again.")

		

		
		
		
	