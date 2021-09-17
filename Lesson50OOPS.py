'''Creating an Account class for our goal tracking app
Now that we have seen how to create a class, let's try making another.

You may have been thinking while doing the previous lesson, that a class would be a great solution to our goal tracking app issues! If we have an account class, we can create an object for each account, and then store its name and balance and add functions so we don't have to repeat as much code. Yes!'''


class Account:

    def __init__(self, name, balance, goal):
        self.name = name
        self.balance = balance
        self.goal = goal

