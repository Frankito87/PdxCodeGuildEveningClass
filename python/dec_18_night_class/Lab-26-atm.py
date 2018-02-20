class ATM:
    def __init__(self, balance=0, interest_rate=0.1):
        self.balance = balance
        self.interest_rate = interest_rate

    def check_balance(self):
        return self.balance

    def deposits(self, amount):
        self.balance += amount
        return amount

    def check_withdrawal(self, amount):
        if amount > self.balance:
            print("Your transaction for {} is not permitted. Please check your balance first !".format(amount))
        else:
            print("Your transaction for {} was accepted.".format(amount), True)
            self.balance -= amount

    def withdrawal(self, amount):
        self.balance -= amount
        return amount

    # I = Prt
    # Where:
    # P = Principal Amount
    # I = Interest Amount
    # r = Rate of Interest per year in decimal;
    # r = R / 100
    # R = Rate of Interest per year as a percent;
    # R = r * 100
    # t = Time Periods involved

    def calc_interest(self, time):
        self.time = time
        total = self.balance * (self.interest_rate / 100) * time
        return total

    def print_transactions(self):
        transactions_list = []
        d = self.deposits(1500)
        b = self.withdrawal(50)
        transactions_list.append(("User deposited ${}".format(d), ("User withdrawal ${}".format(b))))
        return transactions_list

    def play_again(self):
        ask = input("What would you like to do\n:"
                    " 1.Deposit,"
                    "2.Withdraw,"
                    " 3.Check Balance,"
                    " 4.History,"
                    " 5.Calculate Interest!?")
        if ask in '1':
            self.deposits(1500)
            print(a.check_balance())
            self.play_again()
        if ask in '2':
            self.withdrawal(50)
            print(a.check_balance())
            self.play_again()
        if ask in '3':
            self.check_balance()
            print(a.check_balance())
            self.play_again()
        if ask in '4':
            self.print_transactions()
            print(self.print_transactions())
            self.play_again()
        if ask in '5':
            self.calc_interest(5)
            print(self.calc_interest(5))
            self.play_again()
        else:
            quit()


a = ATM(9000, 3.875)
a.play_again()
# a.check_balance()
# print(a.check_balance())
# a.deposits(1500)
# print(a.check_balance())
# a.check_withdrawal(450)
# print(a.check_balance())
# a.withdrawal(50)
# print(a.check_balance())
# print(a.calc_interest(5))
# print(a.print_transactions())


