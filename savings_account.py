import account
class SavingsAccount(Account):
    def __init__(self,balance):
        Account.__init__(self,balance)

    def withdraw(self,balance):
        if amount < limit:
            super().withdraw(amount)
        else:
            print("Amount exceeds limit")