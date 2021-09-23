'''LEARN
Adding a method to update the goal progress
Alright, the last step for our methods is to write one that will calculate the progress the user has made towards their goal for the account.

We haven't used an attribute to store the progress because we always have the goal and the balance so it can be calculated any time the balance changes.

This method will be called by the update_balance() function we wrote in our GUI code. We will edit that later, but for now we will need the method to calculate what % of the goal we have in the account, and return that value.

CREATE
Under the relevant comment define a new method called get_progress() with only self as a parameter.
Inside the method, create a variable called progress. Store the result of calculating (the balance divided by the goal) times 100 in it.
Return the progress variable.
Test it out by adding a print statement to the end that calls get_progress() on the savings account.
Click RUN to test it.
TIPS
You should see 4.0% as we have $40 remaining in the account and the goal is $1000.'''


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

    # Get progress method calculates goal progress
    def get_progress(self):
        progress = (self.balance / self.goal) * 100
        return progress


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
print(savings.get_progress())

