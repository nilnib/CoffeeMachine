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
}
#common functions
def calculation():
    quarter = float(input("How many quarters?: "))
    dimes = float(input("How many dimes?: "))
    nickles = float(input("How many nickles?: "))
    penny = float(input("How many pennies?: "))
    total = quarter * 0.25 + dimes * 0.10 + nickles * 0.05 + penny * 0.01
    return total

def report(resource,money):
    water = resource["water"]
    milk = resource["milk"]
    coffee = resource["coffee"]
    print(f"Water: {water}ml" )
    print(f"Milk: {milk}ml")
    print(f"coffee: {coffee}g")
    print(f"money: ${money}")

#Trying something new:
def makeCoffee(menu,resource,coffeeType):
    coffeeWater = menu[coffeeType]["ingredients"]["water"]
    coffeeBeans = menu[coffeeType]["ingredients"]["coffee"]
    if coffeeType == "espresso":
        coffeeMilk = 0
    else:
        coffeeMilk = menu[coffeeType]["ingredients"]["milk"]
    if resource["water"] >= coffeeWater:
        if resource["coffee"] >= coffeeBeans:
            if resource["milk"] >= coffeeMilk:
                #done
                print("all good")
                total = calculation()
                if total >= menu[coffeeType]["cost"]:
                    change = round(total - menu[coffeeType]["cost"], 2)
                    print(f"Here is ${change} in change")
                    print(f"Here is your {coffeeType}. Enjoy!")
                    return "Positive"
                else:
                    print("Sorry That's not enough money. Money refunded")
                    return "Neutral"
            else:
                print("There is not enough milk")
                return "Negative"
        else:
            print("There is not enough coffee")
            return "Negative"
    else:
        print("There is not enough water!")
        return "Negative"

# def espresso(menu,resource):
#     print(menu["espresso"]["ingredients"])
#     if (resource["water"] - menu["espresso"]["ingredients"]["water"]) >=50 and resource["coffee"]- menu["espresso"]["ingredients"]["coffee"] >=18:
#         print("all good")
#         total = calculation()
#         if total >= menu["espresso"]["cost"]:
#             change = round(total - menu["espresso"]["cost"],2)
#             print(f"Here is ${change} in change")
#             print("Here is your espresso. Enjoy!")
#
#         else:
#             print("Sorry That's not enough money. Money refunded")
#     else:
#         print("Sorry there is not enough resource.")



# User Input at the start of coffemachine


secret = "on"
money = 0

while secret != "off":
    user_choice =input("What would you like? (espresso/latte/cappuccino):").lower().strip()
    if user_choice == "report":
        report(resources,money)
    # elif user_choice == "espresso":
    #     espresso(MENU,resources)
    #     money += 1.5
    #     # Update resource
    #     resources["water"] -=  50
    #     resources["coffee"] -=  18
    elif user_choice == "off":
        secret ="off"
    else:
        is_continue = makeCoffee(MENU, resources, user_choice)
        if is_continue == "Positive":
            #add money to the pot
            money += MENU[user_choice]["cost"]
            #update resources
            resources["water"] -=  MENU[user_choice]["ingredients"]["water"]
            resources["coffee"] -=  MENU[user_choice]["ingredients"]["coffee"]
            if user_choice != "espresso":
                resources["milk"] -= MENU[user_choice]["ingredients"]["milk"]
        elif is_continue == "Neutral":
            continue
        else:
            secret = "off"


report(resources, money)






