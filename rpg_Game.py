import random, time, os, math


def check_input(item):
    if user_input.lower() == item:
        return True
    else:
        return False


def empty():
    print("")
    return


def clear_screen():
    for i in range(1, 20):
        empty()
    return


def help():
    clear_screen()
    print("Choose one of the actions presented on the screen and select one of them")
    print("by typing the action after the \"What would you want to do?: \" message.")
    empty()
    empty()
    empty()
    user_input = input("Press ENTER to dismiss")
    user_choice()


def access_inv():

    '''Access the user inventory and load the current items'''


def access_travel():

    '''Access the travelling screen and load the current position on the map'''


def access_gear():

    '''Access the users gear and load the current gear'''


def user_choice():
    global user_input

    clear_screen()
    empty()
    empty()
    print("Type \"help\" anytime to acces the help menu or \"settings\" to acces the settings menu")
    empty()
    empty()
    print("Inventory    |    Gear")
    print("Travel       |    Exit")
    empty()
    user_input = input("What would you want to do?: ")

    if check_input("inventory"):
        access_inv()

    elif check_input("travel"):
        access_travel()

    elif check_input("gear"):
        access_gear()

    elif check_input("exit"):
        exit()

    elif check_input("help"):
        help()


user_choice()
