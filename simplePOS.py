# Simple application that allows users to order food
# A dictonary that holds the menu items and their price
menu = {
    'White Coffee':1.99,
    'Black Coffee':1.99,
    'Tea':1.00,
    'Latte':2.35,
    'Cappuccino':2.35,
    'Soft Drink':1.35
}
# A simple function that will show the items of the dictonary
def showMenu():
    print("Menu items:\n")
    for k, v in menu.items():
        print(k, v)
    print()

# A function that will ask the user to select an item and then store it in an array
def getUserChoice():
    userChoices = []
    # A while loop that will check if user selects a valid item, or wishes to finish their order
    while True:
        userChoice = input("Please select an item to order (or 'done' to finish):\n> ")
        if userChoice in menu.keys():
            userChoices.append(userChoice)
        elif userChoice.lower() == 'done':
            break
        else:
            print("Please select a valid item to order")
    return userChoices

# A function that will calculate the total order price based of the userChoices array
def calculateTotal(userChoices):
    total = 0
    for choice in userChoices:
        total += menu[choice]
    return total

# Displaying the functions to user
showMenu()
userChoices = getUserChoice()
total = calculateTotal(userChoices)

# Printing out results to 2 decimal places
print(f"The total price of your order is: £{total:.2f}")




