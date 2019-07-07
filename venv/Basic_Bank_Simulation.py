from abc import ABCMeta, abstractmethod
from random import randint

# Creating Abstract Base Class
class Account(metaclass= ABCMeta):

    @abstractmethod # Abstract Method created.
    def createAccount():
        return 0

    @abstractmethod
    def authenicateUser():
        return 0

    @abstractmethod
    def withDrawl():
        return 0

    @abstractmethod
    def desposite():
        return 0

    @abstractmethod
    def checkBalance():
        return 0

class SavingsAccount(Account): # Inheritance performed.

    def __init__(self): # maintianing users
        # [key][0] => name; [key][1] => balance
        self.savingAccounts = {}

    def createAccount(self, name, initialDeposit): # Encapsulation and Overriding performed.
        self.accountNum = randint(1000, 9999)
        self.savingAccounts[self.accountNum] = [name, initialDeposit]
        print('Account created successfully. Your account number is: ', self.accountNum)

    def authenicateUser(self, name, accountNumber):
        if accountNumber in self.savingAccounts.keys(): # Checking if user exists...
            if self.savingAccounts[accountNumber][0] == name:
                print('Authentication Successful')
                self.accountNum = accountNumber
                return True
            else:
                print('Authentication Failed')
                return False
        else: # if user don't exists...
            print('Authentication Failed')
            return False

    def withDrawl(self, withdrawlAmount):
        if withdrawlAmount > self.savingAccounts[self.accountNum][1]: # checking withdrawl amount value
            print('Insufficient Balance')
        else:
            self.savingAccounts[self.accountNum][1] -= withdrawlAmount
            print('Withdraw Successful!')
            self.checkBalance() # Donot Repeat Yourself (DRY) performed...

    def desposite(self, depositeAmount):
        self.savingAccounts[self.accountNum][1] =+ depositeAmount
        print('Amount Desposited.')
        self.checkBalance()

    def checkBalance(self):
        print('Your Balance: ', self.savingAccounts[self.accountNum][1])


savingsAccount = SavingsAccount()
while True:
    print('Enter 1 to Create a new account') # Main Menu
    print('Enter 2 to access your account')
    print('Enter 3 to exit')
    userChoice = int(input())
    if userChoice is 1:
        print('Enter yout name:', end= ' ')
        name = input()
        print('Enter initial deposit:', end= ' ')
        deposit = int(input())
        savingsAccount.createAccount(name, deposit) # Layer of abstraction being provided...
    elif userChoice is 2:
        print('Enter your name:', end= ' ')
        name = input()
        print('Enter your accounr number:', end= ' ')
        accNumber = int(input())
        authenticationStatus = savingsAccount.authenicateUser(name, accNumber)
        if authenticationStatus is True:
            while True:
                print('Enter 1 to withdraw money')
                print('Enter 2 to deposite money')
                print('Enter 3 to check balance')
                print('Enter 4 to go back to main menu')
                userInput = int(input())
                if userInput is 1:
                    print('Enter withdrawl amount:', end=' ')
                    withdrwalAmount = int(input())
                    savingsAccount.withDrawl(withdrwalAmount)
                elif userInput is 2:
                    print('Enter deposit amount:', end=' ')
                    despositAmount = int(input())
                    savingsAccount.desposite(despositAmount)
                elif userInput is 3:
                    savingsAccount.checkBalance()
                elif userInput is 4:
                    break
    elif userChoice is 3:
        quit()











