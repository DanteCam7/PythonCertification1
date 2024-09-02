def addition():
    n1 = int(input("Number 1: "))
    n2 = int(input("Number 2: "))
    print(n1 + n2)
    print("Thanks for adding" + n1)


try:
    #Code we want to try
    #addition()
    print("hola")
except TypeError:
    #Code to be executed if there is an error
    print("You're trying to mix different data types")
except ValueError:
    print("That is not a number")
else:
    #Code will be executed it there is no error
    print("You did all correct")
finally:
    #Code that will be executed anyway
    print("That was all")

def ask_number():

    while True:
        try:
            number = int(input("Give me a number: "))
        except:
            print("That is not a number")
        else:
            print(f"You typed the number {number}")
            break
    print("Thank you")

ask_number()