from Bank_Accounts import *

Dave = BankAccount(2000, "Dave")
Sara = BankAccount(3000, "Sara")

Dave.getBalance()
Sara.getBalance()

Dave.deposite(500)

Dave.withdraw(100)

Dave.transfer(1000, Sara)

jim = interestRewardAcc(1000, "jim")
jim.getBalance()
jim.deposite(100)
jim.transfer(100,Dave)

Blaze = savingAcc(1000, "Blaze")
Blaze.getBalance()
Blaze.deposite(100)
Blaze.transfer(1000, jim)
