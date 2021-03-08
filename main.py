from phoneBook import PhoneBook
import os
import json


def menu():
    print("Choose an option\n"
          "1. Display\n"
          "2. Add contact\n"
          "3. Update contact\n"
          "4. Delete contact\n"
          "5. Exit\n")
    choice = int(input("Choose{1 or 2 or 3 or 4 or 5}:  "))
    return choice


def display():
    filename = "phoneNumber.json"
    # Displaying contacts
    if os.path.exists(filename):
        with open(filename, "r") as file:
            data_from_json = json.load(file)

        if type(data_from_json) is dict:
            data_from_json = [data_from_json]

        for i in data_from_json:
            print(i["name"] + ": " + i["PhoneNumber"])
            # for key, value in i.items():
            #     print(key, value)
            #     print("")
        print("\n")
    else:
        print("Sorry no such file")


def do_choice(k):
    if k == 1:
        display()
    elif k == 2:
        name = str(input("Enter name: "))
        number = str(input("Enter number: "))
        phone_book = PhoneBook(name, number)
        phone_book.save_number_to_json()
    elif k == 3:
        name = str(input("Enter number to change: "))
        phone_book2 = PhoneBook(name, number=None)
        print("Do you wanna create new number or name(1-> name, 2->number): ")
        b = int(input("New number: "))
        if b == 1:
            name1 = input("Enter new name: ")
            phone_book2.updating_the_given_number(name1)
        elif b == 2:
            number1 = input("Enter new number: ")
            phone_book2.updating_the_given_number(None, number1)
        else:
            print("Sorry!!")

    elif k == 4:
        name = input("Name or contact to delete: ")
        phone_book_3 = PhoneBook(name)
    else:
        print("Wrong choice")


# if choice is not 1 or choice is not 2 or choice is not 3
if __name__ == '__main__':
    filename = "phoneNumber.json"

    if os.path.exists(filename):
        display()
        l = 0
        while l != 5:
            k = menu()
            if k == 5:
                break
            else:
                do_choice(k)
        # if k == 1:
        #     print("Sorry No contacs yet")
        # elif k == 2:
        #     name = str(input("Enter name: "))
        #     number = str(input("Enter number: "))
        #     phone_book = PhoneBook(name, number)
        #     phone_book.save_number_to_json()
        # elif k == 3:
        #     name = str(input("Enter number to change: "))
        #     phone_book2 = PhoneBook(name, number=None)
        #     print("Do you wanna create new number or name(1-> name, 2->number): ")
        #     b = int(input("New number: "))
        #     if b == 1:
        #         name1 = input("Enter new name: ")
        #         phone_book2.updating_the_given_number(name1)
        #     elif b == 2:
        #         number1 = input("Enter new number: ")
        #         phone_book2.updating_the_given_number(None, number1)
        #     else:
        #         print("Sorry!!")
        #
        # elif k == 4:
        #     name = input("Name or contact to delete: ")
        #     phone_book_3 = PhoneBook(name)
        # else:
        #     print("Wrong choice")

    else:
        l = 0
        while l != 5:
            print("Sorry no contact storage found")
            print()
            n = int(input("Press (1) if you wanna continue: "))
            if n == 1:
                k = menu()
                if k == 5:
                    break
                else:
                    do_choice(k)
            else:
                pass