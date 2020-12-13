class BankAccount:
    def __init__(self, username_from_bankaccount='placeholder_username', balance_from_bankaccount=0, int_rate_from_bankaccount='1%'):
        self.username = username_from_bankaccount
        self.balance = balance_from_bankaccount
        self.int_rate = int_rate_from_bankaccount
        
    def make_deposit(self, amount):
        self.balance += amount
        return self
    def make_withdrawal(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
            self.balance -= 5
            self.display_user_balance()
            return self
        else:
            self.balance -= amount
            return self
    def display_user_balance(self):
        print(f"{self.username}'s account balance: ${self.balance}.")
        return self
    def transfer_money(self, other_user, amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)
        return self
    def yield_interest(self):
        if self.balance > 0:
            self.balance *= 1.01
        return self
    
        
drake = BankAccount("Drake", 1000)
jay = BankAccount("Jay-Z", 1000)
wayne = BankAccount("Lil Wayne", 1000)


wayne.yield_interest().display_user_balance()

drake.make_deposit(1000).make_deposit(2000).make_deposit(15000).yield_interest().display_user_balance()
jay.make_deposit(20000).make_deposit(5000).make_withdrawal(3000).make_withdrawal(6000).make_withdrawal(23000).make_withdrawal(2000).yield_interest().display_user_balance()