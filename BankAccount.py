'''
Created on Nov 26, 2023

@author: jer21551
'''
class BankAccount:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__balance}")
        else:
            print("Invalid deposit amount. Please enter a positive value.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.__balance}")
        elif amount <= 0:
            print("Invalid withdrawal amount. Please enter a positive value.")
        else:
            print("Insufficient funds. Withdrawal unsuccessful.")

    def get_balance(self):
        return self.__balance
    
def main():
    my_account = BankAccount()
    #create instances of BankAccount class for Tom, Sue, and Bob
    tom_account = BankAccount()
    sue_account = BankAccount()
    bob_account = BankAccount()

    #set starting balance
    tom_starting_balance = float(input("Tom, enter your starting balance: "))
    sue_starting_balance = float(input("Sue, enter your starting balance: "))
    bob_starting_balance = float(input("Bob, enter your starting balance: "))

    tom_account.deposit(tom_starting_balance)
    sue_account.deposit(sue_starting_balance)
    bob_account.deposit(bob_starting_balance)

    #tom pay and deposit
    tom_pay = float(input("Tom, how much were you paid this week? "))
    tom_account.deposit(tom_pay)
    print("I will deposit that into your account.")
    print(f"Tom, your account balance is ${tom_account.get_balance():,.2f}")

    #sue pay and deposit
    sue_pay = float(input("Sue, how much were you paid this week? "))
    sue_account.deposit(sue_pay)
    print("I will deposite that into your account.")
    print(f"Sue, your account balance is ${sue_account.get_balance():,.2f}")

    #bob pay and deposit
    bob_pay = float(input("Bob, how much were you paid this week? "))
    bob_account.deposit(bob_pay)
    print("I will deposit that into your account.")
    print(f"Bob, your account balance is ${bob_account.get_balance():,.2f}")

    #tom withdrawal
    tom_withdrawal = float(input("Tom, how much would you like to withdraw? "))
    tom_account.withdraw(tom_withdrawal)
    print("I will withdraw that amount from your account.")
    print(f"Tom, your account balance is ${tom_account.get_balance():,.2f}")

    #bob withdrawal
    bob_withdrawal = float(input("Bob, how much would you like to withdraw ?"))
    bob_account.withdraw(bob_withdrawal)
    print("I will withdraw that amount from your account.")
    print(f"Bob, your account balance is ${bob_account.get_balance():,.2f}")

    #sue withdrawal
    sue_withdrawal = float(input("Sue, how much would you like to withdraw? "))
    sue_account.withdraw(sue_withdrawal)
    print("I will withdraw that amount from your account.")
    print(f"Sue, your account balance is ${sue_account.get_balance():,.2f}")

#run main function if script is executed
if __name__ == "__main__":
    main()

#TEST INFO: 2 loops, 1 if else (4 point), 2 boolean (4 point), 12 vocab, 1 function (10 point)
