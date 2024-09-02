import sys
import numbers


def ask():
    print("Welcome to Python's DrugStore")
    while True:
        print("[P] - Perfumery\n[F] - Pharmacy\n[C] - Cosmetic")
        try:
            my_answer = input("Choose an option: ").upper()
            ["P", "F", "C"].index(my_answer)
        except ValueError:
            print("Please choose a valid option")
        else:
            break

    numbers.decorator(my_answer)


def start():

    while True:
        ask()
        try:
            other_turn = input("Do you want to take another turn? [S] [N]: ").upper()
            ["S", "N"].index(other_turn)
        except ValueError:
            print("Please choose a valid option")
        else:
            if other_turn == "N":
                print("Thanks for your visit")
                sys.exit()


start()
