from account import Account

class SavingsAccount(Account):
    def __init__(self, balance):
        Account.__init__(self, balance)

    def withdraw(self, amount):
        if amount < 4000 :
            super().withdraw(amount)
        else:
            print("You have exceeded your limit")