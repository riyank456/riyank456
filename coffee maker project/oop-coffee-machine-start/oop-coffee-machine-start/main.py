from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine




off = False
office_coffee = CoffeeMaker()
register = MoneyMachine()


while(off != True):
    menu = Menu() 
    order = input(f"What would you like? {menu.get_items()}\n")
    if(order == "report"):
        office_coffee.report()
        register.report()
    elif(order == "off"):
        off = True
    else:
        customer_drink = menu.find_drink(order)
        if(customer_drink != None):
            water = customer_drink.ingredients['water']
            coffee = customer_drink.ingredients['coffee']
            milk = customer_drink.ingredients['milk']
            if(office_coffee.is_resource_sufficient(customer_drink)): 
                has_enough = register.make_payment(customer_drink.cost)
                if(has_enough == True):
                    office_coffee.make_coffee(customer_drink)


