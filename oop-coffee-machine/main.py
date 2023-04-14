from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
#One note is tht two methods have been usesd in comparison

is_on: bool = True
# TODO 1. Print Report
# TODO 2. Check Resources
# TODO 3. Process Coins
# TODO 4. Check Transaction
# TODO 5. Make Coffee
cm = CoffeeMaker()
mm = MoneyMachine()

while is_on:

    print(f"Hi there what would you like to drink:")
    m = Menu()
    print(m.get_items())
    order_name = input("Order:")
    order = m.find_drink(order_name)

    if order != '':
        if order_name == 'report':
          cm.report()
          mm.report()

        elif cm.is_resource_sufficient(order):

            if mm.make_payment(order.cost):
                cm.make_coffee(order)

# else:
#  if order_name == 'report':
#     cm.report()


