class Persona:
    def __init__(self,name,surname):
        self.name = name
        self.surname = surname

class Client(Persona):

    def __init__(self, name, surname, account_number, balance = 0):
        super().__init__(name, surname)
        self.account_number = account_number
        self.balance = balance
    def __str__(self):
        return f"Client: {self.name} {self.surname}\nAccount balance of {self.account_number}: ${self.balance}"

    def deposit(self, amount_deposited):
        self.balance += amount_deposited
        print("Deposit accepted\n")

    def retired(self,amount_retired):
        if self.balance >= amount_retired:
            self.balance -= amount_retired
            print("Amount retired accepted")
        else:
            print("Insufficient funds")

def create_client():
    name_cl=input('Insert your Name: ')
    surname_cl = input('Insert your Surname: ')
    account_number = input("Insert your account number: ")
    client = Client(name_cl,surname_cl,account_number)
    return client

def beginning():
    my_client = create_client()
    print(my_client)
    option = 0
    while option != 'S':
        print('Choose: Deposit (D), Retire (R), or Exit (S)')
        option = input()

        if option == 'D':
            amount_dep = int(input("Amount to deposit: "))
            my_client.deposit(amount_dep)
        elif option == 'R':
            amount_ret = int(input("Amount to retire: "))
            my_client.retired(amount_ret)
        print(my_client)

    print("Thanks for being with us Bank Python")

beginning()