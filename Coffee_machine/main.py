from data import resources,MENU
from art import logo
profit=0
def resource_check(order_ingredients):
    is_enough = True
    for ingredient in order_ingredients:
        if order_ingredients[ingredient]>=resources[ingredient]:
            print(f"Sorry, you don't have enough {ingredient}")
            is_enough= False
    return is_enough

def process_coins():
    print("Please insert coins")
    total=int(input("How many quaters?"))*0.25
    total+=int(input("How many dimes?"))*0.1
    total+=int(input("How many nickels?"))*0.05
    total+=int(input("How many pennies?"))*0.01
    return total

def transaction_check(money_received,cost):
    if money_received>=cost:
        change=round(money_received-cost,2)
        print(f"Here is your change: {change}, Thank you")
        global profit
        profit+=cost
        return True
    else:
        print("Sorry, you don't have enough money, money refunded!!")
        return False

def make_coffee(drink_name,order_ingredients):
    for ingredient in order_ingredients:
        resources[ingredient]-=order_ingredients[ingredient]
    print(f"Here is your drink: {drink_name} ☕️")


is_on=True
while is_on:
    print(logo)
    order = input("Welcome, what would you like to have today\n Espresso: $1.5 \n Latte: $2.5 \n Capuccino: $3.0\n").lower()
    if order=='off':
        print("Machine Turned off")
        is_on=False
    elif order=='report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}\n\n")
    else:
        drink=MENU[order]
        if resource_check(drink['ingredients']):
            payment=process_coins()
            if transaction_check(payment,drink['cost']):
                make_coffee(order,drink['ingredients'])
