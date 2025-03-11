class Bank_Account:
    def __init__(self,acc_holder_name,acc_number,balance,pin):
        self.account_holder_name = acc_holder_name
        self.account_number = acc_number
        self.balance = balance
        self.__pin = pin

    def getUserDetails(self):
        accNumber = input("Enter Your Account number : ")
        pin = input("Enter Your PIN : ")
        print("")
        try:
            assert int(accNumber) == self.account_number and pin == self.__pin
            print(f"account holder name : {self.account_holder_name}".title())
            print(f"account number : {self.account_number}".title())
            print(f"current balance : {self.balance}".title())

        except AssertionError:
            print("account number or pin wrong plz try again")

    def deposit(self):
        accNumber = input("Enter Your Account number : ")
        pin = input("Enter Your PIN : ")
        print("")
        try:
            assert int(accNumber) == self.account_number and pin == self.__pin
            print(f"current balance : {self.balance}".title())
            print("")
            depositAmount = int(input("enter deposit amount : ".title()))
            self.balance += depositAmount
            print(
                f"current balance after the deposit money : {self.balance}".title())
        except AssertionError:
            print("account number or pin wrong plz try again")

    def withdraw(self):
        accNumber = input("Enter Your Account number : ")
        pin = input("Enter Your PIN : ")
        print("")
        try:
            if int(accNumber) == self.account_number and pin == self.__pin:

                withdrawAmount = int(input("enter withdraw amount : ".title()))

                try:
                    assert self.balance > withdrawAmount
                    self.balance -= withdrawAmount
                    print(
                        f"current balance after the withdraw money : {self.balance}".title())

                except AssertionError:
                    print("Your account don't have sufficient balance")
        except AssertionError:
            print("account number or pin wrong plz try again")
    
a = Bank_Account("Ram", 123456, 20000, "64710")

while True:

    operation = int(input("""
                          
        1. Get User Details 
        2. Deposit Money
        3. Withdraw Money
        4. break loop
                                     
        Select the operation number: """))
    print("")
    match operation:

        case 1:
            a.getUserDetails()

        case 2:
            a.deposit()

        case 3:
            a.withdraw()

        case 4:
            break

    




