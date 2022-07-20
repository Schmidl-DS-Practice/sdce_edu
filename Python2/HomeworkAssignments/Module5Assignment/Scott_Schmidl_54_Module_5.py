# Scott Schmidl - COMP 661 - Programming with Python II - 04/12/2021 to 06/10/2021 - Section 1.3 Module 1 Assignment

import random
import sys

ITEMS_FILENAME = "wizard_all_items.txt"
INVENTORY_FILENAME = "wizard_inventory.txt"

def read_items():
    items = []
    try:
        with open(ITEMS_FILENAME) as file:
            for line in file:
                line = line.replace("\n", "")
                items.append(line)
    except:
        print('Could not find items file\nExiting program. Bye!')
        sys.exit()
    return items

def read_inventory():
    inventory = []
    try:
        with open(INVENTORY_FILENAME) as file:
            for line in file:
                line = line.replace("\n", "")
                inventory.append(line)
    except:
        print('Could not find inventory file!\nWizard is starting with no inventory.\n')
    return inventory

def write_inventory(inventory):
    with open(INVENTORY_FILENAME, "w") as file:
        for item in inventory:
            file.write(item + "\n")

def display_title():
    print("The Wizard Inventory program")
    print()

def display_menu():
    print("COMMAND MENU")
    print("walk - Walk down the path")
    print("show - Show all items")
    print("drop - Drop an item")
    print("exit - Exit program")
    print()

def walk(inventory):
    items = read_items()
    item = random.choice(items)
    print("While walking down a path, you see " + item + ".")
    choice = input("Do you want to grab it? (y/n): ")
    if choice == "y":
        if len(inventory) >= 4:
            print("You can't carry any more items. " +
                    "Drop something first.\n")
        else:
            inventory.append(item)
            print("You picked up " + item + ".\n")
            write_inventory(inventory)

def show(inventory):
    for i in range(len(inventory)):
        item = inventory[i]
        number = i + 1
        print(str(number) + ". " + item)
    print()

def drop_item(inventory):
    try:
        number = int(input("Number: "))
        if number < 1 or number > len(inventory):
            print("Invalid item number.\n")
        else:
            item = inventory.pop(number-1)
            print("You dropped " + item + ".\n")
            write_inventory(inventory)
    except:
        print('Invalid item number.\n')

def main():
    display_title()
    display_menu()

    inventory = read_inventory()
    while True:
        command = input("Command: ")
        if command == "walk":
            walk(inventory)
        elif command == "show":
            show(inventory)
        elif command == "drop":
            drop_item(inventory)
        elif command == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")
    print("Bye!")

if __name__ == "__main__":
    main()
