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

    def transfer(self, amount, account):
        try:
            print("\n**********\n\nBeginning Transfer.." )
            self.vaibleTransction(amount)
            self.withdraw(amount)
            account.deposite(amount)
            print("\nTransfer Successfully..\n\n******")
        except BalanceExcepiton as error:
            print(f"\Transfer interrupted {error}")

class interestRewardAcc(BankAccount):
    def deposite(self, amount):
        self.balance = self.balance +(amount * 1.05)
        print("\nDeposite Successfully")
        self.getBalance()

class savingAcc(interestRewardAcc):
    def __init__(self, InitiallAmount, AccountName):
        super().__init__(InitiallAmount, AccountName)
        self.fee = 5
    
    def withdraw(self, amount):
        try:
            self.vaibleTransction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print("\nWithdraw Successfully")
            self.getBalance()
        except BalanceExcepiton as error:
            print(f"\Withdraw interrupted {error}")

