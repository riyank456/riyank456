total_money = 0
cost = 2.50
resources = {
        "milk": 200,
        "coffee" : 100 ,
        "water" : 300 
    }

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0
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

options = ["espresso", "latte", "cappuccino"]

def prompt():
    customer_drink = input("What would you like? (espresso, latte, cappuccino)\n")
    return customer_drink


def insert_quarters():
    return int(input("how many quarters? \n"))

def insert_dimes():
    return int(input("how many dimes? \n"))

def insert_nickels():
    return int(input("how many nickels? \n"))

def insert_pennies():
    return int(input("how many pennies? \n"))

off = False
while(off != True):
    response = prompt()
    if(response.lower() in options ):
        water = MENU[response]['ingredients']['water']
        coffee = MENU[response]['ingredients']['coffee']    
        milk = MENU[response]['ingredients']['milk'] 
        if((milk < resources['milk']) and ((water < resources["water"])  and (coffee < resources["coffee"]))  ): 
            print("Please insert coins")
            q = insert_quarters()*.25
            d = insert_dimes()*.10
            n = insert_nickels()*.05
            p = insert_pennies()*.01
            total_payment = (q+d+n+p)
            if(total_payment < MENU[response]['cost']):
                print("Sorry that's not enough money. Money refunded.")
            elif(total_payment > MENU[response]['cost']):
                resources['water'] = (resources['water'] - water)
                resources['coffee']  = resources['coffee']  - coffee
                resources['milk'] = resources['milk'] - milk
                change = round(((total_payment-MENU[response]['cost'])), 2)
                total_money = total_money +  MENU[response]['cost']
                print(f"Here is ${change} in change.\n Enjoy your {response}!")
                
            else:
                resources['water'] = (resources['water'] - water)
                resources['coffee']  = resources['coffee']  - coffee
                resources['milk'] = resources['milk'] - milk
                total_money = total_money +  MENU[response]['cost']
                print(f"Here is $0.0 in change. Enjoy your {response}!")
        else:
            if(milk > resources['milk']):
                print("Not enough milk")
            elif(water > resources['water']):
                print("not enough water")
            else:
                print("Not enough coffee")
    elif(response.lower() == "off" ):
        off = True
    elif(response.lower() == "report"):
        waterStatus = resources['water']
        coffeeStatus = resources['coffee']
        milkStatus = resources['milk']
        print(f"Water: {waterStatus}ml \nMilk: {milkStatus}ml \n Coffee: {coffeeStatus}g \nMoney: ${total_money}")
