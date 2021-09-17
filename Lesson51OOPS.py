'''Creating an instance of the class
Ok, we have our class and our __init__ method. Now let's create some instances of it.

Remember that although the __init__ method always has the self parameter, we don't need to pass anything in for it when we instantiate the class, we just need to have the right number of other parameters.'''

'''Outside the class, create an instance of the class called savings and pass in the name Savings, 0 for the balance, and 1000 for the savings goal.
Create another instance of the class for a Phone account with a $800 goal.
Do the same for a Holiday account with a $7000 goal.
Test it out by printing one attribute for each object and clicking RUN'''


# Create the Account class
class Account:
  def __init__(self, name, balance, goal):
    self.name = name
    self.balance = balance
    self.goal = goal

# Create instances of the class
savings =Account("Savings" , 0 ,1000)
phone =Account ("Phone" , 0, 800)
holiday = Account ("Holiday" , 0, 7000)


# Print out some attributes
print(savings.name)
print(phone.balance)
print(holiday.goal)