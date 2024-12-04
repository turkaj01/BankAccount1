class BankAccount:
    bankAccounts=[]
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance): 
        self.balance = balance
        self.int_rate = 0.01
        BankAccount.bankAccounts.append(self)
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        # your code here
        self.balance = self.balance + amount
        return self

    def withdraw(self, amount):
        # your code here
        if self.balance >= amount:
            self.balance = self.balance - amount
        else:
            self.balance = self.balance - 5
            print("Insufficient funds: Charging a $5 fee")
        return self
    def display_account_info(self):
        # your code here
        balance = self.balance
        print("Balance: ", self.balance)
        return self
    def yield_interest(self):
        # your code here
        self.balance = self.balance * self.int_rate + self.balance
        return self

    @classmethod
    def printInstances(cls):
        for i in cls.bankAccounts:
            print( f'The balance is {i.balance} and the interest rate is {i.int_rate}')

account_1 = BankAccount(0.01, 10000)
account_2 = BankAccount(0.01, 5000)


account_1.deposit(500).deposit(200).deposit(2000).withdraw(400).yield_interest().display_account_info()
account_2.deposit(300).deposit(700).withdraw(100).withdraw(200).withdraw(50).withdraw(2000).yield_interest().display_account_info()


BankAccount.printInstances()