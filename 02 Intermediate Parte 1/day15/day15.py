"""
Coffee Machine
"""
# ################ Exercise 1 ####################
# Coffee Machine - Eu
"""
hot1 = {
    'Price': '1.50',
    'Flavour': 'Espresso',
    'Water': '50',
    'Coffee': '18',
    'Milk': '0',
    }

hot2 = {
    'Price': '2.50',
    'Flavour': 'Latte',
    'Water': '200',
    'Coffee': '24',
    'Milk': '150',
    }
hot3 = {
    'Price': '3.00',
    'Flavour': 'Cappuccino',
    'Water': '250',
    'Coffee': '24',
    'Milk': '150',
    }
tank = {
    'Money': '0',
    'Water': '300',
    'Coffee': '100',
    'Milk': '200',
    }

def escolher_cafe():
    global hot1, hot2, hot3
    pedido = input('What would you like? (espresso/latte/cappuccino): ').lower()
    while pedido == 'report':
        print(f"Water:{tank['Water']}ml\nCoffee:{tank['Coffee']}g\nMilk:{tank['Milk']}ml\nMoney: ${tank['Money']}")
        pedido = input('What would you like? (espresso/latte/cappuccino): ')
    if pedido == 'espresso':
        print(f"Your choice: {hot1['Flavour']}\nPrice: {hot1['Price']}.")
        return hot1
    elif pedido == 'latte':
        print(f"Your choice: {hot2['Flavour']}\nPrice: {hot2['Price']}.")
        return hot2
    elif pedido == 'cappuccino':
        print(f"Your choice: {hot3['Flavour']}\nPrice: {hot3['Price']}.")
        return hot3

def pay_coffee():
    global tank
    pedido2 = escolher_cafe()
    pedido2['price'] = float(pedido2['Price'])
    pedido2['Water'] = int(pedido2['Water'])
    pedido2['Coffee'] = int(pedido2['Coffee'])
    pedido2['Milk'] = int(pedido2['Milk'])
    tank['Money'] = float(tank['Money'])
    tank['Water'] = int(tank['Water'])
    tank['Coffee'] = int(tank['Coffee'])
    tank['Milk'] = int(tank['Milk'])
    total_coin += int(input('How many quarters?: ')) * 0.25
    total_coin += int(input('How many dimes?: ')) * 0.10
    total_coin += int(input('How many nickles?: ')) * 0.05
    total_coin += int(input('How many pennies?: ')) * 0.01

    if total_coin == pedido2['price']:
        if tank['Water'] < pedido2['Water'] or tank['Coffee'] < pedido2['Coffee'] or tank['Milk'] < pedido2['Milk']:
            print('Not enough ingredients')
        elif tank['Water'] >= pedido2['Water'] and tank['Coffee'] >= pedido2['Coffee'] and tank['Milk'] >= pedido2[
            'Milk']:
            tank['Water'] -= pedido2['Water']
            tank['Coffee'] -= pedido2['Coffee']
            tank['Milk'] -= pedido2['Milk']
            tank['Money'] += pedido2['price']
            print(f"Here is your {pedido2['Flavour']}.")
    elif total_coin > pedido2['price']:
        if tank['Water'] < pedido2['Water'] or tank['Coffee'] < pedido2['Coffee'] or tank['Milk'] < pedido2['Milk']:
            print('Not enough ingredients')
        elif tank['Water'] >= pedido2['Water'] and tank['Coffee'] >= pedido2['Coffee'] and tank['Milk'] >= pedido2[
            'Milk']:
            tank['Water'] -= pedido2['Water']
            tank['Coffee'] -= pedido2['Coffee']
            tank['Milk'] -= pedido2['Milk']
            tank['Money'] += pedido2['price']
            troco = total_coin - pedido2['price']
            print(f"Here is ${round(troco, 2)} in change.\nHere is your {pedido2['Flavour']}.")
    elif total_coin < pedido2['price']:
        falta = pedido2['price'] - total_coin
        print(f"Sorry. Not enought cash. It miss ${falta}.")

while input('Do you want a coffee? Type \'Yes\' or \'No\': ').lower() == 'yes':
    pay_coffee()
"""
# ################ Exercise 1 ####################
# Coffee Machine - Dr. Angela Yu
"""
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
    },
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"​Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


is_on = True

while is_on:
    choice = input("​What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
"""
