'''Docstrings for documenting classes
We already know about writing comments to document our code. With classes, we usually write docstrings to say what the purpose of the class is. You might remember these from looking at functions in level 2.

A docstring is a description written on the first line of a class (or function) in triple double quotes: """
class MyClass:
  """Here is a description of what this class does"""
If you call help() on a class you will see the docstring e.g. print(help(MyClass))'''


'''create
On line 3, add a docstring to the account class with the following text: The Account class stores the details of each account and has methods to deposit, withdraw and calculate progress towards the savings goal
Underneath the printed attributes from the 3 account objects we created, call the help() function on the Account class and print the result.'''


# Create the Account class
class Account:
  """The Account class stores the details of each account and has methods to deposit, withdraw and calculate progress towards the savings goal"""

  def __init__(self, name, balance, goal):
    self.name = name
    self.balance = balance
    self.goal = goal


# Create instances of the class
savings = Account("Savings", 0, 1000)
phone = Account("Phone", 0, 800)
holiday = Account("Holiday", 0, 7000)

# Print out some attributes
print(savings.name)
print(phone.balance)
print(holiday.goal)
print(help(Account))