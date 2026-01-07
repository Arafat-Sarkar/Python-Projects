class BalanceExcepiton(Exception):
    pass

class BankAccount:
    def __init__(self, InitiallAmount, AccountName):
        self.balance = InitiallAmount
        self.Name = AccountName
        print(f"\nAccount '{self.Name}' Created.\nBalance = ${self.balance:.2f}")

    def getBalance(self):
        print(f"\nAccount '{self.Name}' Balance ${self.balance:.2f}")

    def deposite(self, amount):
        self.balance = self.balance + amount
        print("\n Deposite Compeletd ")
        self.getBalance()

    def vaibleTransction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceExcepiton(
                f"\nSorry , account '{self.Name}' only has balance of {self.balance:.2f}"
            )
        
    def withdraw(self, amount):
        try:
            self.vaibleTransction(amount)
            self.balance = self.balance - amount
            print("\nWithdraw Successfully")
            self.getBalance()
        except BalanceExcepiton as error:
            print(f"\nWithdraw interrupted {error}")