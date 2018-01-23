class BankAccount:
    def __init__(self, name, account_number):
        self.client_name = name
        self.balance = 0
        self.account_number = account_number

    def deposit(self, amount):
        self.balance += amount
        print('Thanks {}! Your balance is now ${}.'.format(self.client_name, self.balance))

    def withdraw(self, amount):
        if self.balance - amount > 0:
            self.balance -= amount
            print('Thanks {}! Your balance is now ${}.'.format(self.client_name, self.balance))
        else:
            print('Sorry {}. You do not have enough funds. Your balance is ${}.'.format(self.client_name, self.balance))


chris = BankAccount('Chris', '000001')
katie = BankAccount('Katie', '000002')
chris.deposit(100)
chris.withdraw(101)
katie.deposit(250)
katie.withdraw(200)