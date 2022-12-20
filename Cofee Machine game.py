MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 25,
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
    "money": 0,
}
end = False
while not end:
    chosen = input("What would you like? (espresso/latte/cappuccino):").lower()
    if resources["water"] < MENU[chosen]["ingredients"]["water"]:
        print("Sorry, not enough water")
        end = True
    if resources["milk"] < MENU[chosen]["ingredients"]["milk"]:
        print("Sorry, not enough milk")
        end = True
    if resources["coffee"] < MENU[chosen]["ingredients"]["coffee"]:
        print("Sorry, not enough coffee")
        end = True
    ingredients = MENU[chosen]["ingredients"]
    for item in ingredients:
        amount = ingredients[item]
        resources[item] -= amount
#while not end:
    print("Please insert coins")
    cost = MENU[chosen]["cost"]
    #print(cost)
    quarters = int(input("How many quarters?:"))
    dimes = int(input("How many dimes?:"))
    nickels = int(input("How many nickels?:"))
    pennies = int(input("How many pennies?:"))

    quarters_in_dollars = float(quarters * 0.25)
    dimes_in_dollars = float(dimes * 0.1)
    nickels_in_dollars = float(nickels * 0.05)
    pennies_in_dollars = float(pennies * 0.01)

    paid = quarters_in_dollars + dimes_in_dollars + nickels_in_dollars + pennies_in_dollars
    #print(paid)
    change = round(paid - cost, 2)
    if cost == paid:
        print(f"You have ${change} in change")
        print(f"Here is your {chosen}. Enjoy! 😊")
        resources["money"] += paid
        #print(resources)
    elif cost > paid:
        print("Too low! Money refunded")
    elif cost < paid:
        print(f"You have ${change} in change")
        print("Change refunded")
