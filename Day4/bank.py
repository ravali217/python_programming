class BankAccount:
    def __init__(self,balance=0):
        self.__balance=balance
        
    def deposit(self,amount):
        self.__balance+=amount
        print(f"the total amount:{amount}")
    def withdraw(self,amount):
        if amount<=self.__balance:
            self.__balance-=amount
            print(f"the withdraw:{amount}")
        else:
            print("money is insufficient balance")

    def get_balance(self):
        print(self.__balance)
ob=BankAccount()
ob.deposit(1000)
ob.withdraw(10)
ob.get_balance()
