class BankAccount:
    def __init__(self):
        self.a_name = "Ram"
        self.a_num = 1234567891
        self.balance = 10000
        self.pin = 64710
    
    def bank_detais(self,pin):
        if(self.pin == 64710):
            print("Account Holder Name: ",self.a_name)
            print("Account Number:",self.a_num)
            print("Total Balance: ",self.balance)

    
    def deposit(self,amount):
        pin = int(input("Enter the Pin "))
        if(pin == 64710):
            print(f"{amount} rupees are successfully added to your account: ")
            self.balance += amount
        else:
            print("Enter the valid pin")
    
    def withdraw(self, Amount):
        pin = int(input("Enter the Pin "))
        if(pin == 64710):
            if(Amount > self.balance):
                print("Your account don’t have sufficient balance.")
            else:
                print(f"{Amount} rupees has been withdrawn successfully")
                self.balance -= Amount
        else:
            print("Enter the valid pin")
        

b1=BankAccount()
b1.bank_detais(64710)
print()
b1.deposit(200)
print()
b1.bank_detais(64710)
print()
b1.withdraw(12000)
print()
b1.withdraw(8000)
print()
b1.bank_detais(64710)


