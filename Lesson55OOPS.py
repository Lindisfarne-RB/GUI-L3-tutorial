'''Write a withdraw method for the Account class
Now let's add a method for withdrawing money from an account. This method should let us withdraw money as long as there is enough in there.

We will check whether the amount to withdraw is less than or equal to the account balance. If so, we will return True, if not we will return False.

CREATE
Complete the tasks below under the relevant comments.

Define a new method called withdraw() that takes the parameters self and amount.
Inside the method, write an if statement to check if the amount is greater than 0 AND if there is enough money in the account to withdraw.
In the if branch (if there is enough money), subtract the amount from the account balance and return True.
In the else branch, return False.
Test the method by calling it on the savings account with the value 10 and then printing the balance.
Test it again by withdrawing 1200 and printing the balance.
Click RUN to check it works correctly.
'''


# Create the Account class
class Account:
    """The Account class stores the details of each account and has methods to deposit, withdraw and calculate progress towards the savings goal"""

    def __init__(self, name, balance, goal):
        self.name = name
        self.balance = balance
        self.goal = goal

    # Deposit method adds money to balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        else:
            return False

    # Withdraw method subtracts money from balance
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return True
        else:
            return False


# Create instances of the class
savings = Account("Savings", 0, 1000)
phone = Account("Phone", 0, 800)
holiday = Account("Holiday", 0, 7000)

# Print out some attributes
print(savings.name)
print(phone.balance)
print(holiday.goal)
print(help(Account))

# Test the deposit method
savings.deposit(50)
print(savings.balance)
savings.withdraw(10)
print(savings.balance)
savings.withdraw(1200)
print(savings.balance)

