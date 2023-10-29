class BankAccount:
    def __init__(self, AccountNumber, name, registration, balance):
        self.AccountNumber = AccountNumber
        self.name = name
        self.registration = registration
        self.balance = balance

    def checkBalance(self):
        print(self.balance)

    def withdraw(self, money):
        self.balance -= money
        print("you have withdraw $" + str(money))
        print("balance left: $" + str(self.balance))

    def deposit(self, money):
        self.balance += money
        print("you have deposited $" + str(money))
        print("balance: $" + str(self.balance))

    def transfer(self, payee, amount):
        self.balance -= amount
        payee.balance += amount
        print("$" + str(amount) + "has been transferred from" + self.name + "to" + payee.name)


var1 = BankAccount("1234", "Clarissa", "144032020", 1000)
var2 = BankAccount("2222", "bob", "12031920", 20)

var1.checkBalance()
var2.checkBalance()

var1.deposit(99)
var1.withdraw(20)
var1.transfer(var2,100)