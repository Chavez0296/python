class BankAccount:
    def __init__(self, account_balance):
        self.account_balance = account_balance
    def deposit(self, depo):
        try:
            if depo <= 0:
                raise ValueError("Error! Deposits must be nonnegative!")
            else:
                self.account_balance += depo
        except ValueError as e:
            print(f"{e}")
    def withdraw(self,amnt):
        try:
            if amnt < 0:
                raise ValueError("Error! Withdrawals must be nonnegative!")
            else:
                self.account_balance -= amnt
        except ValueError as e:
            print(f"{e}")
    def __str__(self):
        return f"Your account balance is ${self.account_balance}"
        
bank = BankAccount(500)
print(bank.account_balance)
print(bank)
bank.deposit(-1)
bank.withdraw(-50)
bank.deposit(50)
print(bank)
bank.withdraw(25)
print(bank)